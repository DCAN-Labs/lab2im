import os
import sys
from os import listdir
from os.path import isfile, join

import nibabel as nib
import gzip
import shutil
from contextlib import ExitStack


def fix_unzipped_files(input_folder):
    os.chdir(input_folder)
    only_files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    for f in only_files:
        try:
            nib.load(f)
        except Exception as ex:
            print(ex)
            with ExitStack() as stack:
                new_name = f[:-3]
                os.rename(f, new_name)
                # noinspection PyTypeChecker
                f_in = stack.enter_context(open(new_name, 'rb'))
                f_out = stack.enter_context(gzip.open(new_name + '.gz', 'wb'))
                shutil.copyfileobj(f_in, f_out)
                os.remove(new_name)


if __name__ == "__main__":
    fix_unzipped_files(sys.argv[1])
