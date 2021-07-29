# Code written by Daniel Jimenez-Sanchez.
# This method is described in https://arxiv.org/abs/2103.05385

from PatchContrastiveLearning.utils.DatasetParameters import parameters
from PatchContrastiveLearning.patch_contrastive_learning import patch_contrastive_learning
from PatchContrastiveLearning.preprocess_images import preprocess_images

def main(path):
    # Select Experiment parameters
    params = parameters(path)
    
    # Preprocess Images
    preprocess_images(path,params['PCL_ZscoreNormalization'],params['PCL_patch_size'])

    # Patch Contrastive Learning
    patch_contrastive_learning(path,params)    
    
if __name__ == "__main__":
    path = '/gpu-data/djsanchez/PCL/examples/Example_POLE/'            
    main(path)
 