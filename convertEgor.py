import nibabel as nib
import numpy as np

def nifti_to_numpy(fname_in, ras_to_rcp=False):
    """
​
    Args:
        fname_in: str
            Full path to the input file.
        ras_to_rcp: bool
            Whether to convert from RAS+ to row-column-plane coordinates.
​
    Returns:
        spacings: 3-tuple of float
            (pixel spacing in r, pixel spacing in c, slice thickness).
​
    """
    scan = nib.load(fname_in)
    stack = scan.get_fdata()
    spacings = [scan.affine[i, i] for i in range(3)]
    if ras_to_rcp:
        stack = np.moveaxis(stack, [2, 1, 0], [0, 1, 2])
        spacings = [-s for s in spacings[::-1]]

    return stack, spacings


def numpy_to_nifti(stack, fname_out, spacings=None, rcp_to_ras=False):
    """
​
    Args:
        stack: (r, c, p) ndarray
            Data array.
        fname_out:
            Full path to the output file.
        spacings: 3-tuple of float
            (pixel spacing in r, pixel spacing in c, slice thickness).
        rcp_to_ras: bool
            Whether to convert from row-column-plane to RAS+ coordinates.
    """
    if not rcp_to_ras:
        affine = np.eye(4, dtype=np.float)
        if spacings is not None:
            affine[0, 0] = spacings[0]
            affine[1, 1] = spacings[1]
            affine[2, 2] = spacings[2]
    else:
        stack = np.moveaxis(stack, [0, 1, 2], [2, 1, 0])
        affine = np.diag([-1., -1., -1., 1.]).astype(np.float)
        if spacings is not None:
            affine[0, 0] = -spacings[2]
            affine[1, 1] = -spacings[1]
            affine[2, 2] = -spacings[0]
    scan = nib.Nifti1Image(stack, affine=affine)
    nib.save(scan, fname_out)
