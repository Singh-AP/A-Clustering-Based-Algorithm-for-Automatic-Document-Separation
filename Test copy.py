
# -----------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torch.autograd import Variable
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torch.utils.data.dataset import Dataset
import time
image_size = 224

# class CustomDatasetFromImages(Dataset):
#     def __init__(self, csv_path, transforms):
#         # Read the csv file
#         self.data_info = pd.read_csv(csv_path)
#         # First column contains the image paths
#         self.image_array = np.asarray(self.data_info.iloc[:, 0])
#         # Second column is the labels
#         self.label_array = np.asarray(self.data_info.iloc[:, 1])
#         # Calculate len
#         self.data_len = len(self.data_info.index)
#         self.transforms = transforms

#     def __getitem__(self, index):
#         # Get image name from the pandas df
#         single_image_name = self.image_array[index]
#         img_as_img = cv2.imread(single_image_name, 0)

#         #####This area for testing of various image preprocessing techniques#####
#         # Always end with img_resized for easy modularity#

#         ###Histogram Equalization###
#         equ = cv2.equalizeHist(img_as_img)
#         img_resized = cv2.resize(equ, (image_size, image_size))


#         ###Image Header###
#         #height, width = img_as_img.shape
#         #img_header = img_as_img[0:(int(height*0.33)), 0:width]
#         #img_resized = cv2.resize(img_header, (image_size, image_size))

#         ###Image Center###
#         #img_center = img_as_img[int(height*0.33):int(height*0.67),int(width*0.25):int(width*0.75)]
#         #img_resized = cv2.resize(img_center, (image_size, image_size))

#         img_final = np.expand_dims(img_resized, 0)
#         single_image_label = self.label_array[index]
#         # Return image and the label
#         return (img_final, single_image_label)


#     def __len__(self):
#         return self.data_len

def GetImage(imgdir):
    img_as_img = cv2.imread(imgdir, 0)

    #####This area for testing of various image preprocessing techniques#####
    # Always end with img_resized for easy modularity#

    ###Histogram Equalization###
    equ = cv2.equalizeHist(img_as_img)
    img_resized = cv2.resize(equ, (image_size, image_size))


    ###Image Header###
    #height, width = img_as_img.shape
    #img_header = img_as_img[0:(int(height*0.33)), 0:width]
    #img_resized = cv2.resize(img_header, (image_size, image_size))

    ###Image Center###
    #img_center = img_as_img[int(height*0.33):int(height*0.67),int(width*0.25):int(width*0.75)]
    #img_resized = cv2.resize(img_center, (image_size, image_size))

    img_final = np.expand_dims(img_resized, 0)
    # single_image_label = self.label_array[index]

    # Return image and the label
    return img_final


# if __name__ == '__main__':
    # train_loader = CustomDatasetFromImages('/home/ubuntu/MachineLearningII/train_images_and_labels.csv', transforms = transforms)
#     test_loader = CustomDatasetFromImages('test_images_and_labels.csv', transforms = transforms)

# #transform = transforms.Compose([transforms.ToPILImage(), transforms.ToTensor()])

# num_epochs = 10
# batch_size = 10
# learning_rate = 0.001

# train = DataLoader(train_loader, batch_size = batch_size, shuffle=True)
# test = DataLoader(test_loader, batch_size = batch_size, shuffle=True)

# train_iter = iter(train)
# test_iter = iter(test)

# images, labels = train_iter.next()

# num_epochs = 10
# batch_size = 50
# learning_rate = 0.001

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            #1 input for grayscale, # of feature maps,
            nn.Conv2d(1, 32, kernel_size=7, padding=3, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.layer4 = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.layer5 = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        
        self.fc1 = nn.Linear(7 * 7 * 32, 256)
        self.drop1 = nn.Dropout(0.2)
        self.fc2 = nn.Linear(256, 16)

    def forward(self, x):
        out = self.layer1(x.float())
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        # print("out4", out.shape)
        out = self.layer5(out)
        # print("out5", out.shape)
        out = out.view(out.size(0),-1 )
        out=out.reshape((1,32,32))
        out=nn.UpsamplingNearest2d(scale_factor=(1.0/32.0))(out)
        out=nn.UpsamplingNearest2d(size=(49))(out)
        out=nn.UpsamplingNearest2d(scale_factor=32.0)(out)
        
        
        out = self.fc1(out)
        out = self.drop1(out)
        out = self.fc2(out)
        return torch.sigmoid(out)

def infer(imgdir):
    cnn = CNN()

    cnn.load_state_dict(torch.load("cnn-wholeimage-224-4ConvBlocks-0000001lr-7kernel-Adam-10Epochs-50batchsize.pkl"))
    # Test the Model
    cnn.eval()  # Change model to 'eval' mode (BN uses moving mean/var).
    # correct = 0
    # total = 0

    # im_labels = []
    # im_preds = []
    images=GetImage(imgdir)
    print((images.shape))
    images=cv2.resize(images,dsize=(1,7))
    images=images.reshape((32,1,7,7))
    # for i, (images, labels) in enumerate(test_iter):
    images = Variable(torch.tensor(images))
    outputs = cnn(images)
    print(outputs.data.size() )
    _, predicted = torch.max(outputs.data, 1)
    # total += labels.size(0)
    # correct += (predicted.cpu() == labels).sum()

    # if (i) % 10 == 0:
    #     print('Epoch {}/{}, Iter {}/{}, Loss: {}'.format(epoch + 1, num_epochs, i, (test_loader.data_len / batch_size),
    #                                                     loss.item()))

    # im_labels.append(labels.cpu().numpy())
    # im_preds.append(predicted.cpu().numpy())
    print(predicted.size())
    print("category =",predicted)
    return predicted

# # -----------------------------------------------------------------------------------
# print('Test Accuracy of the model on the test images: {}'.format(100 * correct / total))
# # -----------------------------------------------------------------------------------
# # Save the Trained Model
# #torch.save(cnn.state_dict(), 'cnn-wholeimage-50-5ConvBlocks-5Kernel-3fc2DropsHistEq-5Epochs-50batchsize.pkl')
# #torch.save(cnn.state_dict(), 'cnn-wholeimage-224-4ConvBlocks-00001lr-11kernel-Adam.pkl".pkl')

# preds = [x for pred in im_preds for x in pred]
# labels = [x for label in im_labels for x in label]

# from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score, classification_report

# cm = confusion_matrix(labels, preds)
# print(cm)

# acc = accuracy_score(labels, preds, sample_weight=None)
# print("Accuracy: " + str(acc))

# f1 = f1_score(labels, preds, average='macro')
# print("F1: " + str(f1))
# recall = recall_score(labels, preds, average='macro')
# print("Recall: " + str(recall))
# precision = precision_score(labels, preds, average='macro')
# print("Precision: " + str(precision))

# weights = []
# for i in range(32):
#     kernel = cnn._modules['layer1']._modules['0'].weight.data[i][0].cpu().numpy()
#     weights.append(kernel)

# flat_weights = []
# for weight in weights:
#     flat_weight = [x for row in weight for x in row]
#     flat_weights.append(flat_weight)

# weights_df = pd.DataFrame(flat_weights)
# weights_df.to_csv('/home/ubuntu/MachineLearningII/Weights/50imsize.csv')

infer("Layout_Features/novel.png")
print('Done')
