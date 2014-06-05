# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.model import Binarize

def test_Binarize_inputs():
    input_map = dict(abs=dict(argstr='--abs',
    ),
    args=dict(argstr='%s',
    ),
    bin_col_num=dict(argstr='--bincol',
    ),
    bin_val=dict(argstr='--binval %d',
    ),
    bin_val_not=dict(argstr='--binvalnot %d',
    ),
    binary_file=dict(argstr='--o %s',
    genfile=True,
    ),
    count_file=dict(argstr='--count %s',
    ),
    dilate=dict(argstr='--dilate %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    erode=dict(argstr='--erode  %d',
    ),
    erode2d=dict(argstr='--erode2d %d',
    ),
    frame_no=dict(argstr='--frame %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='--i %s',
    copyfile=False,
    mandatory=True,
    ),
    invert=dict(argstr='--inv',
    ),
    mask_file=dict(argstr='--mask maskvol',
    ),
    mask_thresh=dict(argstr='--mask-thresh %f',
    ),
    match=dict(argstr='--match %d...',
    ),
    max=dict(argstr='--max %f',
    xor=['wm_ven_csf'],
    ),
    merge_file=dict(argstr='--merge %s',
    ),
    min=dict(argstr='--min %f',
    xor=['wm_ven_csf'],
    ),
    out_type=dict(argstr='',
    ),
    rmax=dict(argstr='--rmax %f',
    ),
    rmin=dict(argstr='--rmin %f',
    ),
    subjects_dir=dict(),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    ventricles=dict(argstr='--ventricles',
    ),
    wm=dict(argstr='--wm',
    ),
    wm_ven_csf=dict(argstr='--wm+vcsf',
    xor=['min', 'max'],
    ),
    zero_edges=dict(argstr='--zero-edges',
    ),
    zero_slice_edge=dict(argstr='--zero-slice-edges',
    ),
    )
    inputs = Binarize.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Binarize_outputs():
    output_map = dict(binary_file=dict(),
    count_file=dict(),
    )
    outputs = Binarize.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

