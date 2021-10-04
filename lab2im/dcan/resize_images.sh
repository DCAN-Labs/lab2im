module load fsl
# flirt -in 0mo_template_01_0000.nii.gz -ref 1mo_sub-198549_0000.nii.gz -out 0mo_template_01_0000_resized.nii.gz -interp spline -applyisoxfm 1 -init $FSLDIR/etc/flirtsch/ident.mat
# flirt -applyisoxfm 1 -init $FSLDIR/etc/flirtsch/ident.mat -in 0mo_template_01.nii.gz -ref 1mo_sub-198549.nii.gz -out 0mo_template_01_resized.nii.gz -interp nearestneighbour

cd /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task510_BCP_ABCD_Neonates_Augmentation/labelsTr/ || exit
for input in 0mo*.nii.gz
  do
    echo "Input file: $input"
    output="../labelsTrResized/${input}"
    echo "Output file: $output"
    flirt -applyisoxfm 1 -init $FSLDIR/etc/flirtsch/ident.mat -in "$input" -ref 1mo_sub-198549.nii.gz -out $output -interp nearestneighbour
  done
