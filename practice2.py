import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from convertEgor import nifti_to_numpy, numpy_to_nifti
from nibabel.affines import apply_affine
import numpy.linalg as npl
import cv2

def transform(point, TransformArray):

    for i in range(0, len(point)-1):
        xyz = point[1]
        p = np.dot(TransformArray, np.transpose(p))
    for i in range(0, len(point)-1):
        point[i] = p[i]
    return point
np.set_printoptions(precision=3, suppress=True)
filename1 = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/3_sag_3d_dess_right.nii'
filename2 = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/7_cor_t1_3d_flash_right.nii'
epi_img = nib.load(filename1)
anat_img = nib.load(filename2)
epi_img_data = epi_img.get_fdata()
anat_img_data = anat_img.get_fdata()


print(epi_img.affine)
print(anat_img.affine)
M = epi_img.affine[:3, :3]
abc = epi_img.affine[:3, 3]
epi_vox_center = (np.array(epi_img_data.shape) - 1) / 2.
result_f = apply_affine(epi_img.affine, epi_vox_center)
epi_vox2anat_vox = npl.inv(anat_img.affine).dot(epi_img.affine)
corresponding = apply_affine(epi_vox2anat_vox, epi_vox_center)

anat_vox_center = (np.array(anat_img_data.shape) - 1) / 2.
print(corresponding)
print(anat_vox_center)
dif = anat_vox_center-corresponding

stack, spacings = nifti_to_numpy(filename1)
stack2, spacings2 = nifti_to_numpy(filename2)
x=dif*spacings2

stackcenter = (np.array(stack.shape) - 1) / 2.



TranformationMatrix = np.identity(4)
TranformationMatrix[:3, 3] = dif

