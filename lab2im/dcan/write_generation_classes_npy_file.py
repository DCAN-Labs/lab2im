import numpy as np


if __name__ == '__main__':
    classes = np.arange(0, 532)
    np.save('/home/miran045/reine097/projects2/lab2im/tutorials/data_example/dcan/generation_classes.npy', classes)
    np.save('/home/miran045/reine097/projects2/lab2im/tutorials/data_example/dcan/generation_labels.npy', classes)
