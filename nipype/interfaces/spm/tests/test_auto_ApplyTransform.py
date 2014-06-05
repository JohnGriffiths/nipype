# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.utils import ApplyTransform

def test_ApplyTransform_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(copyfile=True,
    mandatory=True,
    ),
    mat=dict(mandatory=True,
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    out_file=dict(genfile=True,
    ),
    paths=dict(),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = ApplyTransform.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ApplyTransform_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = ApplyTransform.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

