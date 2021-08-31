import sys
from os import listdir
from os.path import isfile, join

from lab2im.dcan.image_generation import generate_images


def generate_images_from_folder(input_folder, output_folder, priors_folder):
    only_files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    for file_name in only_files:
        generate_images(join(input_folder, file_name), priors_folder, output_folder, 1)


if __name__ == "__main__":
    generate_images_from_folder(sys.argv[1], sys.argv[2], sys.argv[3])
