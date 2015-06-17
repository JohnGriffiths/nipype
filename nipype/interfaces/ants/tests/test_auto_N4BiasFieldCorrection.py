# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.ants.segmentation import N4BiasFieldCorrection

def test_N4BiasFieldCorrection_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bias_image=dict(hash_files=False,
    ),
    bspline_fitting_distance=dict(argstr='--bspline-fitting %s',
    ),
    bspline_order=dict(requires=['bspline_fitting_distance'],
    ),
    convergence_threshold=dict(requires=['n_iterations'],
    ),
    dimension=dict(argstr='--image-dimension %d',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    input_image=dict(argstr='--input-image %s',
    mandatory=True,
    ),
    mask_image=dict(argstr='--mask-image %s',
    ),
    n_iterations=dict(argstr='--convergence %s',
    requires=['convergence_threshold'],
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    output_image=dict(argstr='--output %s',
    genfile=True,
    hash_files=False,
    ),
    save_bias=dict(mandatory=True,
    usedefault=True,
    xor=['bias_image'],
    ),
    shrink_factor=dict(argstr='--shrink-factor %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    weight_image=dict(argstr='--weight-image %s',
    ),
    )
    inputs = N4BiasFieldCorrection.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_N4BiasFieldCorrection_outputs():
    output_map = dict(bias_image=dict(),
    output_image=dict(),
    )
    outputs = N4BiasFieldCorrection.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
