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


# Our workflow followed these stages:
As a reference for our model we were inspired by Ben Saunder's work (https://github.com/BenSaunders27/ProgressiveTransformersSLP) 

1. data collection to create a robust and quantitatively suitable dataset to ensure an efficient model;
2. data aggregation and preprocessing: we gathered multimedia and text files and cleaned the data;
We reported all the core data for training at the following link: https://www.kaggle.com/datasets/lucatorre/listerdata
3. use of the Openpose open source tool for the extraction of joints from the clips;
4. training and testing of the model.


