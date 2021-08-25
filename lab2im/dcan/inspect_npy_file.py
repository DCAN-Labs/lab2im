import numpy as np
import sys


def inspect_npy_file(file_path):
    contents = np.load(file_path)
    print(contents)


if __name__ == '__main__':
    inspect_npy_file(sys.argv[1])
