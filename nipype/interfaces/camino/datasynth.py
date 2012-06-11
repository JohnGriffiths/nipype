"""""
====================================================================
datasynth.py - nipype wrapper for camino diffusion model simulations
====================================================================
        
"""
from nipype.interfaces.base import (traits, TraitedSpec, File, StdOutCommandLine, 
                                    StdOutCommandLineInputSpec, isdefined,
                                    BaseInterface, OutputMultiPath, BaseInterfaceInputSpec)

# from nipype.utils.filemanip import split_filename
import numpy as np
import glob
import os

class AnalyticModelInputSpec(StdOutCommandLineInputSpec):
    
    n_compartments = traits.Int(argstr='compartment %d', units='NA', position=1,
                                desc="Number of compartments " )
    
    compartment1_name = traits.Enum('stick', 'CylinderGPD', 'Gammadistribradiicylinders',
                                    'Ball', 'Zeppelin', 'Tensor', 'Astrosticks', 
                                    'Astrocylinders', 'SphereGPD', 'Dot', argstr='%s',
                                    position=2,desc = 'compartment1_name' )
            
    compartment1_vf = traits.Float(argstr='%1.3f',position=3,desc='compartment1_volume_fraction')
    
    compartment1_params = traits.List(traits.Float,position=4,minlen=0, maxlen=5,argstr='%s',
                                      desc='compartment1_parameters')
    
    compartment2_name = traits.Enum('stick', 'CylinderGPD', 'Gammadistribradiicylinders',
                                    'Ball', 'Zeppelin', 'Tensor', 'Astrosticks', 
                                    'Astrocylinders', 'SphereGPD', 'Dot', argstr='%s',
                                    position=5,desc = 'compartment2_name' )    
    
    compartment2_vf = traits.Float(argstr='%1.3f',position=6,desc='compartment2_volume_fraction')
    
    compartment2_params = traits.List(traits.Float,position=7,minlen=0, maxlen=5,argstr='%s',
                                      desc='compartment2_parameters')
    
    compartment3_name = traits.Enum('stick', 'CylinderGPD', 'Gammadistribradiicylinders',
                                    'Ball', 'Zeppelin', 'Tensor', 'Astrosticks', 
                                    'Astrocylinders', 'SphereGPD', 'Dot', argstr='%s',
                                    position=8,desc = 'compartment3_name' )
    
    compartment3_params = traits.List(traits.Float,position=9,minlen=0, maxlen=5,argstr='%s',
                                      desc='compartment3_parameters')
        
    n_voxels = traits.Int(argstr='-voxels %d', units='NA', desc="Number of voxels to simulate")
    # Check: 'separateruns' option for running a separate simulation in each voxel

    schemefile = traits.File(exists=True, argstr='-schemefile %s',desc = 'scheme file')
    
    out_file = traits.File(desc = 'name of output file (.Bfloat format)')


class AnalyticModelOutputSpec(TraitedSpec):

    synth_data = File(exists=True, desc='simulated_data')
    
class AnalyticModel(StdOutCommandLine):
    """    
    Example: 'ZeppelinCylinderDot model from camino analytic models tutorial
    
    -------
    >>> from nipype.interfaces.camino import datasynth
    >>> zcd = datasynth.AnalyticModel()
    >>> zcd.inputs.n_compartments = 3
    >>> zcd.inputs.compartment1_name = 'CylinderGPD'
    >>> zcd.inputs.compartment1_vf = 0.6
    >>> zcd.inputs.compartment1_params = [1.7E-9, 0.0,0.0,4E-6]
    >>> zcd.inputs.compartment2_name = 'Zeppelin'
    >>> zcd.inputs.compartment2_vf = 0.1
    >>> zcd.inputs.compartment2_params = [1.7E-9,0.0,0.0,2E-10]
    >>> zcd.inputs.compartment3_name = 'Dot'
    >>> zcd.inputs.schemefile = '59.scheme'
    >>> zcd.inputs.n_voxels = 1
    >>> zcd.inputs.out_file = 'sim_data.Bfloat'
    >>> zcd.run()                  # doctest: +SKIP
    """
    
    _cmd = 'datasynth -synthmodel'
    input_spec=AnalyticModelInputSpec
    output_spec=AnalyticModelOutputSpec
    
        
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['synth_data'] = os.path.abspath(self._gen_outfilename())
        return outputs
    
    def _gen_outfilename(self):
        outfilename = self.inputs.out_file
        return outfilename
    


class MonteCarloInputSpec(StdOutCommandLineInputSpec):
    
    walkers = traits.Int(argstr='-walkers %d', position=1,units='NA', desc="Number of " \
                         "spins to use in simulation. Simple simulations require " \
                         "around 10000 spins, but simulations on more complex " \
                         "substrates require more spins to capture the additional " \
                         "complexity, particularly at higher b-values." \
                         "For the simulations covered in this tutorial we recommend" \
                         "AT LEAST 100000 spins, but more may well be required.")
    
    tmax = traits.Int(argstr='-tmax %d', position=2,units='NA', desc="Number of timesteps into " \
                      "which the simulation is divided. This can be thought of as " \
                      "defining the temporal resolution of the simulation, since the total" \
                      "duration of a simulation's dynamics (i.e. the period of time that is " \
                      "simulated, and not how long it takes to run!) is defined by its schemefile." \
                      "This duration will be split into a number of updates of equal length" \
                      "dt. This is an important number, since together with the diffusivity" \
                      "it defines the length of steps in each spin's' random walk."\
                      "It also defines how long a simulation will take to run." \
                      "More timesteps equates to a longer execution. Investigations"  \
                      "have shown that simple substrates require about 1000 updates"\
                      "although very complex substrates and very high b-values "\
                      "may need more (5000 or more).")

    voxels = traits.Int(argstr='-voxels %d', units='NA', position=3,desc="Specifies the number of voxels of "\
                         "data to synthesise. It is important to specify this to be at least 1. By "\
                         "default, a simulation will run once and then fill remaining voxels with "\
                         "different noise-realisations of the synthesised data. To run a separate "\
                         "simulation in each voxel, use the -separateruns option.")

    barrier_permeability = traits.Float(argstr='-p %s', units='NA',position=4, desc="Specifies the probability"\
                                     "that a spin will step through a barrier unaffected instead of"\
                                     "interacting with it. This is usually set to 0, making barriers impermeable.")
    

    schemefile = traits.File(argstr='-schemefile %s', units='NA', position=5,desc="Specifies the scheme file "\
                            "to use for data synthesis. The scheme file describes the pulse sequence "\
                            "used to generate diffusion-weighted data. These specify gradients, "\
                            "pulse durations, orientations, separations, etc. and are no different "\
                            "to those used by other parts of Camino.Specifies the seed for the random number ")

    initial = traits.Enum('uniform', 'intra', 'extra', 'square', 'hex', argstr='-initial %s',position=6,desc="Specificies "\
                          "initial conditions of spins by a keyword. uniform distributes spins uniformly "\
                          "(but randomly) across the substrate. delta locates them all at the same "\
                          "point in the centre of the substrate, intra distributes them uniformly in "\
                          "the intracellular space and extra does the same but in the extracellular "\
                          "space. Note that some substrates do not have a reliable definition of "\
                          "intracellular and extracellular, and in this case the use of intra and "\
                          "extra will lead to unexpected results and is deprecated.")


    substrate = traits.Enum('empty', 'cylinder', 'crossing', 'inflammation', 'ply', argstr='-substrate %s',position=7,desc=" write somethign here")

    substratesize = traits.Float(argstr='-substratesize %s',desc="something to write here")

    ply_file = traits.File(argstr='-plyfile %s', desc='plyfile...')

    increments = traits.Int(argstr='-increments %s',desc="something to write here")
        
    diffusivity = traits.Float(argstr='-diffusivity %d', units='NA', desc="Specifies the free"\
                              "diffusivity for spins in the simulation in SI units. The default" \
                              " value is 2.0E-9m^s/s but this can be changed as needed. All physical" \
                              " quantities in Camino (including b-value) use SI units (seconds, " \
                              "meters, teslas) so it may be necessary to convert to SI before " \
                              "specifying them.")
    
    separateruns = traits.Bool(argstr='-separateruns', desc="Runs a separate simulation in each voxel")
    
    
    seed = traits.Int(argstr='-seed %d', units='NA', desc="Specifies the seed for the random number "\
                       "generators to use. Since it is a Monte-Carlo simulation, it makes extensive "\
                       "use of random numbers when running. Specifying different seeds will cause "\
                       "different sequences of random numbers to be generated and hence different "\
                       "trajectories of spins to be developed as (slightly) different synthetic "\
                       "measurements to be synthesised. A seed can be any integer, although it is "\
                       "better to use large numbers (8 or 9 digits) as more complex seeds give lower "\
                       "correlations in random number sequences.")
    
    duration = traits.Float(argstr='-duration %s', units='NA', desc="Specifies the duration "\
                                       "of the dynamics (in seconds) if no scheme file is used. "\
                                       "You can find out what this should be by using the longest "\
                                       "acquisition in your scheme file. The simulation should be long enough"\
                                       "to run at least from the onset of the first gradient block to the end "\
                                       "of the last.")

    trajectories_file = traits.Either(traits.Bool, traits.File(),hash_files=False, argstr='-trajfile %s', units='NA', desc="Specifies the name of the trajfile "\
                                   "generated. A trajfile contains the complete trajectories of all spins in a "\
                                   "given simulation and may be parsed into a set of measurements at a later date.")

    substrateinfo_file = traits.Either(traits.Bool, traits.File(),hash_files=False, argstr='-substrateinfo > %s', units='NA', desc="Specifies the name of the substrate info file "\
                                   "generated - suffix needs to be '.info'")
    
    crosssection_file  = traits.Either(traits.Bool, traits.File(),hash_files=False, argstr='-drawcrosssection > %s', units='NA', desc="Specifies the name of the cross section file "\
                                   "generated - suffix needs to be '.gray'. Visualize with, e.g., ImageMagik 'Display' function.......")
    
    
    scan = traits.Int(argstr='-scan %d', units='NA', desc="This command reads the trajectories file specified "\
                      "and synthesise diffusion weighted data using myscheme.scheme. Due to the size of the files "\
                      "involved this will take at least several seconds and may take several minutes for larger files.")
    
    packing = traits.Enum('square', 'hex', argstr='-packing %s',desc="The simulation supports both of these configurations,"\
                          "Cylinders in the simulation do not necessarily have to be abutting (i.e. close-packed, so that "\
                          "their edges touch), although this is certainly possible. The size and spacing of cylinders is "\
                          "controlled by the -cylinderrad and -cylindersep options respectively. -cylinderrad specifies "\
                          "the RADIUS of all cylinders and -cylindersep the separation between cylinders. "\
                          "The cylindersep variable is defined as the distance between the central axes of the cylinders "\
                          "and hence must be at least twice the cylinder radius. Separations closer than this will cause "\
                          "cylinders to overlap and intersect and may cause unexpected results. Both distances must be "\
                          "specified in meters (NOT in microns.")
          
    numcylinders = traits.Int(argstr='-numcylinders %s',desc="something to write here")
   
    voxelsizefrac = traits.Float(argstr='-voxelsizefrac %s',desc="something to write here")
    
    stats_file = File(argstr='-statsfile %s', desc="generate a stats file, just specify its name "\
                      "from the command line using -statsfile myStatsFile.dat along with the rest of your simulation command")
      
    cylinder_radius = traits.Float(argstr='-cylinderrad %s',desc="cylinder radius")

    cylinder_separation = traits.Float(argstr='-cylindersep %s',desc="The cylindersep variable is "\
                                       "defined as the distance between the central axes of the cylinders "\
                                       "and hence must be at least twice the cylinder radius. "\
                                       "Separations closer than this will cause cylinders to overlap and "\
                                       "intersect and may cause unexpected results. Both distances must be "\
                                       "specified in meters (NOT in microns).")
    
    crossangle = traits.Float(argstr='-crossangle %s',desc="The crossing angle is specified in radians "\
                                      "(NOT degrees) using the -crossangle 0.7854. This is approximately pi/4,"\
                                      " or 45 degrees. The crossing angle can take on any value, just make sure"\
                                      " you use radians!")

    gamma = traits.List(traits.Float,minlen=2,maxlen=2,argstr='-gamma %s',desc="Gamma distribution parameters")
                        
    #out_file = traits.File(desc = 'name of output file')


class MonteCarloOutputSpec(TraitedSpec):

    synth_data = File(exists=True, desc='simulated_data')
    trajectories_file = File(desc='trajectories file')
    substrateinfo_file = File(desc='substrateinfo_file')
    crossection_file = File(desc='crosssection_file')
    
class MonteCarlo(StdOutCommandLine):
    """
    Example
    -------
    
    >>> import nipype.interfaces.camino.datasynth
    >>> mc = datasynth.MonteCarlo()
    
    >>> mc = datasynth.MonteCarlo()
    >>> mc.inputs.walkers = 100000
    >>> mc.inputs.tmax = 1000
    >>> mc.inputs.barrier_permeability = 0.0
    >>> mc.inputs.voxels = 1
    >>> mc.inputs.initial = 'uniform'
    >>> mc.inputs.schemefile = '59.scheme'
    >>> mc.inputs.substrate = 'inflammation'
    >>> mc.inputs.increments = 1
    >>> mc.inputs.gamma = [1.84037, 7.8E-7]
    >>> mc.inputs.substratesize = 3.5E-5 #0.0000355m = 0.0355mm = 35.5um 
    >>> mc.inputs.numcylinders = 100
    >>> mc.inputs.out_file = 'gammacyls_n100_tester_fixed_code.bfloat'
    >>> mc.cmdline
    """

    _cmd = 'datasynth'
    input_spec=MonteCarloInputSpec
    output_spec=MonteCarloOutputSpec

    def _gen_outfilename(self):
        return "synth_data.Bfloat"
    
    def _gen_filename(self, name):
        if name is 'trajectories_file':
            return 'MC_trajfile.traj'
        else:
            return super(MonteCarlo, self)._gen_filename(name)
    
    def _format_arg(self, name, spec, value):
        if name == 'trajectories_file':
            if isinstance(value, bool):
                if value == True:
                    value = self._gen_filename(name)
                else:
                    return ""
        elif name == 'out_file':            
            if isdefined(self.inputs.trajectories_file) and self.inputs.trajectories_file:
                return ""
            else:
                return super(MonteCarlo, self)._format_arg(name, spec, value)
        return super(MonteCarlo, self)._format_arg(name, spec, value)
    
    def _list_outputs(self):
        outputs = self.output_spec().get()
        if isdefined(self.inputs.trajectories_file) and self.inputs.trajectories_file:
            if isinstance(self.inputs.trajectories_file, bool):
                outputs['trajectories_file'] = os.path.abspath(self._gen_filename("trajectories_file"))
            else:
                outputs['trajectories_file'] = os.path.abspath(self.inputs.trajectories_file)
        elif isdefined(self.inputs.out_file) and self.inputs.out_file:
            outputs['synth_data'] = os.path.abspath(self.inputs.out_file)
        else:   
            outputs['synth_data'] = os.path.abspath(self._gen_filename("out_file"))
        
        if isdefined(self.inputs.subtrateinfo_file) and self.inputs.substrateinfo_file:
                outputs['substrateinfo_file'] = os.path.abspath(self.inputs.substrateinfo_file)
        
        if isdefined(self.inputs.crosssection_file) and self.inputs.crosssection_file:
                outputs['crosssection_file'] = os.path.abspath(self.inputs.crosssection_file)
            
        return outputs #self._outputs_from_inputs(outputs)





class ScanTrajfileInputSpec(StdOutCommandLineInputSpec):
    
    trajfile = traits.File(exists=True, argstr='-trajfile %s',desc = 'trajectories file')
    
    schemefile = traits.File(exists=True, argstr='-schemefile %s',desc = 'scheme file')
    
    out_file = traits.File(desc = 'name of output file (.Bfloat format)')


class ScanTrajfileOutputSpec(TraitedSpec):

    synth_data = File(exists=True, desc='simulated_data')
    
class ScanTrajfile(StdOutCommandLine):
    """    
    Example:
    -------
    >>> from nipype.interfaces.camino import datasynth
    >>> st = datasynth.ScanTrajfile()
    >>> st.inputs.trajfile = <trajectories filename>
    >>> st.inputs.schemefile = < scheme file >
    >>> st.inputs.out_file = < output file > 
    >>> st.run()                  # doctest: +SKIP
    """
    
    _cmd = 'scan '
    input_spec=ScanTrajfileInputSpec
    output_spec=ScanTrajfileOutputSpec
        
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['synth_data'] = os.path.abspath(self._gen_outfilename())
        return outputs
    
    def _gen_outfilename(self):
        outfilename = self.inputs.out_file
        return outfilename
    



















"""
class PlotDataInputSpec(BaseInterfaceInputSpec):
    
    datafile = traits.File(desc = '.Bfloat file')
    
    schemefile = traits.File(desc = 'scheme file')
    
    outfile_name = traits.String(desc = 'name of new file')
    

class PlotDataOutputSpec(TraitedSpec):

    figure = File(desc='plotted data')
    
class PlotData(BaseInterface):
    '''   
    Example:
    -------
    '''
    
    input_spec=PlotDataInputSpec
    output_spec=PlotDataOutputSpec
    
    f = open(self.inputs.datafile)
    f_dat = np.fromfile(f)
        
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['figure'] = os.path.abspath(self._gen_outfilename())
        return outputs
    
    def _gen_outfilename(self):
        outfilename = self.inputs.out_file
        return outfilename
    

"""    




