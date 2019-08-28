import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from convertEgor import nifti_to_numpy, numpy_to_nifti
from nibabel.affines import apply_affine
import numpy.linalg as npl
import cv2
from skimage.transform import AffineTransform, warp

def shift(image, vector):
    transform = AffineTransform(translation=vector)
    shifted = warp(image, transform)

    #shifted = shifted.astype(image.dtype)
    return shifted


filename1 = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/3_sag_3d_dess_right.nii'
filename2 = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/7_cor_t1_3d_flash_right.nii'

epi_img = nib.load(filename1)
anat_img = nib.load(filename2)
epi_img_data = epi_img.get_fdata()
anat_img_data = anat_img.get_fdata()

stack, spacings = nifti_to_numpy(filename2)

TranformationMatrix = np.identity(4)
x = [-10, 15]

#TranformationMatrix[:2, 2] = x

c=len(stack[2:])
stack_modified = np.zeros((512,80,512))
for i in range(512):
    img = stack[:,:,i]
    modified_image = shift(img, x)
    stack_modified[:,:,i] = modified_image
fn = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/7_cor_t1_3d_flash_right_modified.nii'
nifti_modified = numpy_to_nifti(stack_modified,fn ,spacings)
