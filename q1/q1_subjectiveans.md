<h1>Performance of Models</h1>

| Model                                                              | Training Time (sec) | Training Loss | Training Accuracy | Testing Accuracy | Number of Parameters |
|--------------------------------------------------------------------|---------------|---------------|-------------------|------------------|----------------------|
| VGG (1 block)                                                      | 136.79       | 47.5             | 52.5%                | 50%               |81921409            |
| VGG (3 blocks)                                                     | 134.02       | 8.42             | 100%                | 75%               | 20573761            |
| VGG (3 blocks) with data augmentation                             | 137.53       | 0.029             | 98.75%                | 67.5%               | 20573761|
| Transfer learning using VGG16 with tuning all layers              | 30.9435       | 0.7385             | 43.125%                | 50.0%               | 134264641            |
| Transfer learning using VGG16 with tuning only final MLP layers    | 27.626       | 0.1296             | 99.375%                | 97.5%               |119549953 (Trainable)            |
| MLP model                                                          | 134.94      | 0.637             | 51.875%                | 55%               | 248557569           |


<h1>Vgg1</h1>
Image Data
<img src='vgg3/vgg3_imgset.jpg'>
<img src='vgg1/imgset.jpg'>
Accuracy_test
<img src='vgg1/Accuracy_test (1).svg'>
Accuracy_train
<img src='vgg1/Accuracy_train (1).svg'>
Training Loss
<img src='vgg1/Loss_train.svg'>

<h1>VGG3</h1>
<img src='vgg3/vgg3_imgset.jpg'>
<img src='vgg3/imgeval.jpg'>
Accuracy_test
<img src='vgg3/Accuracy_test.svg'>
Accuracy_train
<img src='vgg3/Accuracy_train.svg'>
Training Loss
<img src='vgg3/Loss_train.svg'>

<h1>Vgg3 augmented</h1>
<img src='vgg3/vgg3_imgset.jpg'>
<img src='vgg3da/imgeval.jpg'>
Accuracy_test
<img src='vgg3da/Accuracy_test.svg'>
Accuracy_train
<img src='vgg3da/Accuracy_train.svg'>
Training Loss
<img src='vgg3da/Loss_train.svg'>

<h1>Vgg16(all)</h1>
<img src='vgg3/vgg3_imgset.jpg'>
<!-- <img src='vgg3da/imgeval.jpg'> -->
Accuracy_test
<img src='vgg16/All_Accuracy_test.svg'>
Accuracy_train
<img src='vgg16/All_Accuracy_train.svg'>
Training Loss
<img src='vgg16/All_Loss_train.svg'>

<h1>Vgg16(all)</h1>
<img src='vgg3/vgg3_imgset.jpg'>
<!-- <img src='vgg3da/imgeval.jpg'> -->
Accuracy_test
<img src='vgg16/Freeze_Accuracy_test.svg'>
Accuracy_train
<img src='vgg16/Freeze_Accuracy_train.svg'>
Training Loss
<img src='vgg16/Freeze_Loss_train.svg'>
<h2>Questions</h2>

- **Are the results as expected? Why or why not?**<br>
Vgg3 performend bettter than vgg1 and similiarly vgg16 also performned better  than vgg3. The augmenetd dataset model didnt perform as expected. even though augmentation gives us diverse inputs to train on the test dataset evaluation results doesnt hold up to this expectation. This may be due to the smaller datset size used. The VGG16 models behaved as expected. The MLP model performend poorly as well when compared to vgg3 and vgg16 models.
- **Does data augmentation help? Why or why not?**<br>
Data augmentation helps us in improving the input dataset for training which in theory should help us in training a better model. But in our case the dataset's size was a factor that determined our accuracy.
- **Does it matter how many epochs you fine tune the model? Why or why not?**<br>
As we increase the no of epochs the model tends to overfit the training data. This negatively affects our test accuracy
- **Are there any particular images that the model is confused about? Why or why not?**<br>
  Some images had rabbits of brown color similiar to monkeys these were among the images that got mis classified. 

<h2>MLP vs VGG</h2>
The accuracy received for MLP is lower than that of vgg models. VGG captures spatial features better than MLP which is important for image recognition.
