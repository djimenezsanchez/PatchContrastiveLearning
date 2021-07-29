def parameters(path):
    # Parameters of Patch Contrastive Learning
    # Path: path to the directory where the images are located.

    args={}
    args['path'] = path

    # Choose whether to use a gpu or a cpu. 
    args['device'] = 'cuda:0'
        
    # Output dimensions of the embedding generated from image patches
    args['PCL_embedding_dimensions'] = 256

    # Batch size when training the CNN 
    args['PCL_batch_size']=60

    # Number of epoch utlized to train the CNN
    args['PCL_epochs']=1000

    # Size of image patches.
    args['PCL_patch_size']=15

    # If set to true the CNN learns patches of size ('PCL_patch_size') and patches of size ('PCL_patch_size')*3
    # If set to False the CNN learns patches of size ('PCL_patch_size') i.e., local phenotypes.
    args['PCL_pheno_neigh']=False 

    # Multiplication factor that is applied to patch size to extract image crops. See the manuscript for more information (https://arxiv.org/abs/2103.05385)
    args['PCL_alpha_L']=1.2

    # Z-score normalization to each patch. Calculates mean and std of each patch and normalizes it.
    args['PCL_ZscoreNormalization']=True       

    # Z-score normalization to each image dimension (e.g., marker, channel, target, etc.). Calculates mean and std of each image dimension using all the images in the cohort.
    args['PCL_ZscoreNormalization_Cohort']=True

    # Width of the kernels applied in the CNN
    args['PCL_width_CNN']=2 # Most used values are  (1, 2, 4)

    # Number of convolutional layers in the CNN
    args['PCL_depth_CNN']=101 # Most used values are 50 or 101 for usin ResNet-50 or ResNet-101, respectively. 

    return args