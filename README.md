# Patch contrastive learning (PCL)

This implementation exhaustively finds biology differences within the image dataset using a self-supervised contrastive learning paradigm. When PCL is trained, the dataset is divided into image patches which are encoded into enriched patch embeddings. Image patch embeddings consists of n-dimensional vectors whose euclidean distances are lowest when referring to similar biology structures and the highest when they contain different biology structures.

***Applications:*** 
They are especially useful when data is scarce and can be utilized in custom-made machine learning pipelines with very different objectives:   
  - Discovery of new biological structures
  - Measurement of biological structures across subject-types (e.g., treated vs. control)
  - Patient outcome prediction
  - Subject regression analysis
  - etc.

For more information about this tool please refer to this <a href="arxiv.org/abs/2103.05385">Paper</a>. 

Authors: Daniel Jiménez-Sánchez, Mikel Ariz, Hang Chang, Xavier Matias-Guiu, Carlos E. de Andrea, Carlos Ortiz-de-Solórzano.

<div align="center">
  <img width="90%" alt="Patch contrastive learning" src="https://github.com/djimenezsanchez/PatchContrastiveLearning/blob/main/images/PCL_GITHUB.gif">
</div>
<div align="center">
  An illustration of Patch Contrastive Learning. 
</div>

 
### Data download

To replicate the paper's experiments on a endometrial cancer 7-marker image dataset, first download the images following the [link (download Example_POLE.zip)](https://zenodo.org/record/4630664#.YFoGLa9KiUk).

When downloaded, add the images to the folder 'Examples/Example_POLE/'.

### Usage 

Run main.py 
