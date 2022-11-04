# Sign Language Translation through Pose Detection (Italian to LIS)

Lister is a translation app implemented by Team 4 of the 5G Academy, created with the aim of creating new forms of inclusion for deaf people.
In the everyday life of a sign language speaker, even the simplest interaction can be a stressful moment, and for this reason an instant and on-demand translator was imagined to overcome the language barrier between sign and non-sign language speakers.

Accessibility is guaranteed by a simple and intuitive interface, which allows the user to create ephemeral or permanent chats in which the translation from Italian (text or audio) to LIS is done via a humanoid avatar. 
The accuracy of the translation is ensured by the refinement of the Machine and Deep Learning techniques used to train the neural network that associates word and sign: thanks to a vast multimedia LIS dataset provided by Animundi (RAI), the digitisation of a sign vocabulary, the first goal of the project, was made possible.

In order to make the algorithm autonomous in the recognition of the linguistic components and the subsequent translation via avatar, the technical support of the Urban/Eco interdepartmental research centre was essential: although Lister is a simplification tool, it is in fact its great technological complexity that makes it possible.

# Pipeline Steps

![pipeline_img](https://user-images.githubusercontent.com/117447103/199977486-4b62b49e-5650-40ba-8512-70003a6e3837.jpg)

The application's ability to perform a translation goes through several steps, the first of which is the transcription of the audio input. For the implementation of the first step, we used the open source tool provided by Nvidia NeMo (https://github.com/NVIDIA/NeMo). 

This tool allows through the microphone to transcribe what is said: in the second step, the model will be able to draw from the transcribed text file in order to predict associations between glosses and skels (poses). In the third step, the skeleton files are supplied to the MetaHuman software, a complete framework that creates highly realistic human characters, which will interpret them and generate an avatar that can perform lis translation.


# Workflow stages
As a reference for our model we were inspired by Ben Saunder's work (https://github.com/BenSaunders27/ProgressiveTransformersSLP) 

1. data collection to create a robust and quantitatively suitable dataset to ensure an efficient model;
2. use of the Openpose open source tool for the extraction of joints from the clips, https://github.com/CMU-Perceptual-Computing-Lab/openpose;
3. data aggregation and preprocessing: we gathered multimedia and text files and cleaned the data;
We reported all the core data for training at the following link: https://www.kaggle.com/datasets/lucatorre/listerdata
4. training and testing of the model.

**Data collection** 

In order to crop videos of the Lampadino & Caramella cartoon (season 1, 2) and to isolate the LIS interpreter, we used Avidemux, 
an open source video editing software. We were able to obtain an average of 40 clips per episode composing a dataset of 2,427 videos.

![datasetimage](https://user-images.githubusercontent.com/117447103/200005909-8470e10a-a4d3-49e5-b2cc-57b957456fd1.png)

**OpenPose and joint extraction**

Using the open source tool Openpose, we extracted the joints for all the clips previously cropped.
This operation was performed within a virtual machine because it was computationally very onerous.

![MicrosoftTeams-image](https://user-images.githubusercontent.com/117382704/200009464-5c54a375-1cd4-4b5a-9b5e-2bbeb57bf581.png)


**Data aggregation and preprocessing**

To train the model, we divided the dataset into training, testing and validation. For each split, four different files were created. 
The first file contains the file paths of the clips, the second file contains the sign language gloss and the third file contains the Italian gloss. 
Lastly, the fourth file contains the joints extracted with OpenPose. With respect to the skels data, we have performed a recalculation due to the disparity of joints considered between the work formerly done by Saunders and the data needed by MetaHuman.

![75a1865d-86e1-447b-9778-d40bc458b662](https://user-images.githubusercontent.com/117382704/200009749-8cdea175-7564-49e2-8ce4-a31de96026ca.jpg)

**Training and testing**

We carried out the training and testing of the algorithm with the methods specified in Saunders' paper, of which we report the results in lister/configs.

**Avatar generator**

Once the training of the model was finished, one could proceed by providing the text file as input to the pre-trained neural 
network in order to obtain an association from Italian to Italian Sign Language. 

![MicrosoftTeams-image (1)](https://user-images.githubusercontent.com/117382704/200019487-eafe2ef2-80db-4dd1-b8c6-1d90ffe2f6c6.png)

# Reference
@inproceedings{saunders2020progressive,
	title		=	{{Progressive Transformers for End-to-End Sign Language Production}},
	author		=	{Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
	booktitle   	=   	{Proceedings of the European Conference on Computer Vision (ECCV)},
	year		=	{2020}}

@inproceedings{saunders2020adversarial,
	title		=	{{Adversarial Training for Multi-Channel Sign Language Production}},
	author		=	{Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
	booktitle   	=   	{Proceedings of the British Machine Vision Conference (BMVC)},
	year		=	{2020}}

@inproceedings{saunders2021continuous,
	title		=	{{Continuous 3D Multi-Channel Sign Language Production via Progressive Transformers and Mixture Density Networks}},
	author		=	{Saunders, Ben and Camgoz, Necati Cihan and Bowden, Richard},
	booktitle   	=   	{International Journal of Computer Vision (IJCV)},
	year		=	{2021}}

