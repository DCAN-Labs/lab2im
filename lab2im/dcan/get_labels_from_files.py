import os
import nibabel as nib

label_set = set()
for dirpath, dirs, files in os.walk("/home/miran045/reine097/GATES_SEGS/Jedgroup_atlas_editing/ForLab2Im/"):
	for filename in files:
		fname = os.path.join(dirpath, filename)
		if 'aseg' in fname:
			img = nib.load(fname)
			shape = img.shape
			data = img.get_fdata()
			for i in range(shape[0]):
				for j in range(shape[1]):
					for k in range(shape[2]):
						label_set.add(int(data[i, j, k]))
label_list = list(label_set)
label_list.sort()
print(label_list)
