# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import SUSAN

def test_SUSAN_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    brightness_threshold=dict(argstr='%.10f',
    mandatory=True,
    position=2,
    ),
    dimension=dict(argstr='%d',
    position=4,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fwhm=dict(argstr='%.10f',
    mandatory=True,
    position=3,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    out_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    position=-1,
    ),
    output_type=dict(),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    usans=dict(argstr='',
    position=6,
    usedefault=True,
    ),
    use_median=dict(argstr='%d',
    position=5,
    usedefault=True,
    ),
    )
    inputs = SUSAN.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_SUSAN_outputs():
    output_map = dict(smoothed_file=dict(),
    )
    outputs = SUSAN.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

