from lab2im.image_generator import ImageGenerator


def gen_images():
    brain_generator = ImageGenerator("tutorials/data_example/lab2im/brain_label_map.nii.gz")
    im, lab = brain_generator.generate_image()


if __name__ == '__main__':
    gen_images()
