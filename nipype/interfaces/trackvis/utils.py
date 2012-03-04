"""
utils.py - nipype interfaces for trackvis command line functionalities
======================================================================

                                                         JDG 03/03/2012  
    
Contents:
---------

    - track_transform
    
"""

import os

from nipype.interfaces.base import (CommandLineInputSpec, CommandLine, traits,
                                    TraitedSpec, File)

from nipype.utils.filemanip import split_filename



class track_transform_InputSpec(CommandLineInputSpec):

    input_track_file = File(exists=True, argstr='%s',desc='name of input .trk file', position=1)
    
    output_track_file = traits.String(argstr='%s',genfile=True,Mandatory=False,
                                      desc='name of output .trk file', position=2)    
    
    source_volume = File(exists=True, argstr='-src %s', mandatory=True,
                         desc= "source volume file that the original tracks are "
                         "based on, usually dwi or b0 volume. must be in nifti format")
    
    reference_volume = File(exists=True, argstr='-ref %s', mandatory=True,
                            desc='reference volume file that the tracks are registered'
                            "to. must be in nifti format.")

    
    registration_matrix_file= File(exists=True, argstr='-reg %s', mandatory=True,
                                   desc='registration matrix file')    
    
    registration_type = traits.Enum('flirt', 'tkregister', argstr='-reg_type %s',
                                     desc= """-reg_type, --registration_type <type>
                                     type of the registration matrix. valid inputs 
                                     are 'flirt' or 'tkregister'. default is 'flirt'.""")


    
    invert_reg = traits.Bool(argstr=' -invert_reg ', desc="invert reg",
                             """invert the registration matrix. for 
                             convenience of inverse transformation.""")


class track_transform_OutputSpec(TraitedSpec):
    
    output_track_file = File(exists=True, desc=' Track transform output file ')    

class track_transform(CommandLine):
    """    
    Apply fsl or freesurfer transform to trackvis .trk file, 
    using the trackvis 'track_transform' function. Produces a 
    command line call of the form 
    
       track_transform INPUT_TRACK_FILE OUTPUT_TRACK_FILE [OPTION]...

    
    Examples
    --------

    >>> import nipype.interfaces.trackvis as tv
    >>> tt = tv.track_transform()
    >>> tt.inputs.input_track_file = <filename>
    >>> tt.inputs.source_volume = <filename>
    >>> tt.inputs.reference_volume = <filename>
    >>> tt.inputs.registration_matrix_file = <filename>
    >>> tt.run()                  # doctest: +SKIP
 
    """
    _cmd = 'track_transform '
    input_spec=track_transform_InputSpec
    output_spec=track_transform_OutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['output_track_file'] = os.path.abspath(self._gen_outfilename())
        return outputs

    def _gen_filename(self, name):
        if name is 'output_track_file':
            return self._gen_outfilename()
        else:
            return None
    def _gen_outfilename(self):
        _, name , _ = split_filename(self.inputs.input_track_file)
        return name + '_tt.trk'


