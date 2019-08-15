import nibabel as nib
import matplotlib.pyplot as plt

registered_filename = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/outdir/result.0.nii'
img_result = nib.load(registered_filename)
out1 = img_result.get_fdata()
filenameA = 'C:/Users/Amir Kazemtarghi/Desktop/EGOR/first try/3_sag_3d_dess_right.nii'
img_fix = nib.load(filenameA)
out2 = img_fix.get_fdata()


ax1 = out1[40, :, :]
axx1 = out2[40, :, :]


ax2 = out1[80, :, :]
axx2 = out2[80, :, :]

ax3 = out1[90, :, :]
axx3 = out2[90, :, :]




# add a subplot with no frame
plt.subplot(321)
plt.imshow(ax1, cmap="gray")
plt.subplot(322)
plt.imshow(axx1, cmap="gray")

plt.subplot(323)
plt.imshow(ax2, cmap="gray")
plt.subplot(324)
plt.imshow(axx2, cmap="gray")

plt.subplot(325)
plt.imshow(ax3, cmap="gray")
plt.subplot(326)
plt.imshow(axx3, cmap="gray")
