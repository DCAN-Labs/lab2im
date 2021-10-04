import os
import nibabel as nib
import sys


def print_image_shapes(directory):
    for dirpath, dirs, files in os.walk(directory):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            img = nib.load(fname)
            shape = img.shape
            print('{}: {}'.format(filename, shape))


if __name__ == "__main__":
    print_image_shapes(sys.argv[1])
