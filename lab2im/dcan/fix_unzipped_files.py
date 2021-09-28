import os
from os import listdir
from os.path import isfile, join

import nibabel as nib
import gzip
import shutil
from contextlib import ExitStack

print(nib.__version__)

input_folder = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task509_Paper/labelsTr'
os.chdir(input_folder)
only_files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
for f in only_files:
    try:
        img = nib.load(f)
    except Exception as ex:
        print(ex)
        with ExitStack() as stack:
            new_name = f[:-3]
            os.rename(f, new_name)
            f_in = stack.enter_context(open(new_name, 'rb'))
            f_out = stack.enter_context(gzip.open(new_name + '.gz', 'wb'))
            shutil.copyfileobj(f_in, f_out)
            os.remove(new_name)
