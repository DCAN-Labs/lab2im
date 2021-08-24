import os
import time
from lab2im import utils
from lab2im.image_generator import ImageGenerator
import sys


def main(path_label_map='./data_example/brain_label_map.nii.gz', result_dir='./generated_images', n_examples=5,
         generation_labels='./data_example/generation_labels.npy',
         prior_means='./data_example/prior_means.npy', prior_stds='./data_example/prior_stds.npy'):
    """This tutorials generates 5 synthetic *T1-weighted* brain MRI scans from a label map.
    Specifically, it explains how to impose prior distributions on the GMM parameters, so that we can can generate
    images of desired intensity distribution.  By default the GMM parameters (means and standard deviations of each
    Gaussian), are sampled from uniform distributions of wide predefined ranges, thus yielding output images of random
    contrast.  Here we show how to generate images of desired contrast by imposing the prior distributions from which
    we sample the means and standard deviations of the GMM.

    Keyword arguments:
    path_label_map -- label map to generate images from (default './data_example/brain_label_map.nii.gz')
    result_dir -- the directory where the generated images are written to (default './generated_images')
    n_examples -- general parameter (default 5)
    generation_labels -- specify structures from which we want to generate
                         (default './data_example/generation_labels.npy')
    prior_means -- We specify here the hyperparameters of the prior distributions to sample the means of the GMM. As
                   these prior distributions are Gaussians, they are each controlled by a mean and a standard deviation.
                   Therefore, the numpy array pointed by prior_means is of size (2, K), where K is the nummber of
                   classes specified in generation_classes. The first row of prior_means correspond to the means of the
                   Gaussian priors, and the second row correspond to standard deviations.
                   (default './data_example/prior_means.npy')
    prior_stds -- same as for prior_means, but for the standard deviations of the GMM.
                  (default  './data_example/prior_stds.npy')
    """
    # instantiate BrainGenerator object
    brain_generator = ImageGenerator(labels_dir=path_label_map,
                                     generation_labels=generation_labels,
                                     prior_means=prior_means,
                                     prior_stds=prior_stds)

    # create result dir
    utils.mkdir(result_dir)

    for n in range(n_examples):
        # generate new image and corresponding labels
        start = time.time()
        im, lab = brain_generator.generate_image()
        end = time.time()
        print('generation {0:d} took {1:.01f}s'.format(n, end - start))

        # save output image and label map
        utils.save_volume(im, brain_generator.aff, brain_generator.header,
                          os.path.join(result_dir, 't1_%s.nii.gz' % n))
        utils.save_volume(lab, brain_generator.aff, brain_generator.header,
                          os.path.join(result_dir, 't1_labels_%s.nii.gz' % n))


if __name__ == '__main__':
    pth_lbl_mp = sys.argv[1]
    rslt_dr = sys.argv[2]
    main(pth_lbl_mp, rslt_dr, n_examples=int(sys.argv[3]), generation_labels=sys.argv[4], prior_means=sys.argv[7],
         prior_stds=sys.argv[8])
