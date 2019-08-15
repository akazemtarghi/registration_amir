import nibabel as nib
import numpy as np




filename1 = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/3_sag_3d_dess_right.nii'
filename2 = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/7_cor_t1_3d_flash_right.nii'
epi_img = nib.load(filename1)
anat_img = nib.load(filename2)
epi_img_data = epi_img.get_fdata()
anat_img_data = anat_img.get_fdata()

np.set_printoptions(precision=3, suppress=True)

print(epi_img.affine)
print(anat_img.affine)

M = epi_img.affine[:3, :3]
abc = epi_img.affine[:3, 3]

epi_vox_center = (np.array(epi_img_data.shape) - 1) / 2.

from nibabel.affines import apply_affine
result_f = apply_affine(epi_img.affine, epi_vox_center)

import numpy.linalg as npl
epi_vox2anat_vox = npl.inv(anat_img.affine).dot(epi_img.affine)
a = apply_affine(epi_vox2anat_vox, epi_vox_center)
print(a)
anat_vox_center = (np.array(anat_img_data.shape) - 1) / 2.
print(anat_vox_center)

