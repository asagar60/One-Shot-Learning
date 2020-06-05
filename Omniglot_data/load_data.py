import os
import random
import numpy as np 
import glob
import pickle as pkl
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

from tqdm import tqdm
from time import time
from PIL import Image


class datainfo(): 
  
    # __init__ function 
    def __init__(self, data_dir, isTraining = True): 

        self.data_dir = data_dir 
        self.data_list = []
        self.X = []
        self.y= []
        self.n_classes = 0
        self.n_alphabets = 0
        self.train = isTraining
          
    def load_details(self):
        for dir_ in tqdm(os.listdir(self.data_dir)):
            dirpath_ = os.path.join(self.data_dir, dir_)
            n_chars = len(os.listdir(dirpath_))
            self.n_classes += n_chars
            for subdir_ in os.listdir(dirpath_):
                subdirpath_ = os.path.join(dirpath_, subdir_)
                img_list = glob.glob(subdirpath_+"/*.png")
                
                if len(self.X) == 0:
                    self.X= img_list
                    self.y =[str(dir_+"_"+subdir_)]*len(img_list)
                else:
                    self.X.extend(img_list)
                    self.y.extend([str(dir_+"_"+subdir_)]*len(img_list))
            self.data_list.append([dir_, n_chars])
        self.data_list = np.asarray(self.data_list)
        self.n_alphabets = len(self.data_list)
        self.X = np.asarray(self.X).reshape(-1,1)
        self.y = np.asarray(self.y).reshape(-1,1)
        if self.train == False:
            file_name = "test_dir_data.pkl"
            with open(file_name, "wb") as f:
                pkl.dump((self.X, self.y), f)
            print("Pickle file saved")

  
    
    def visualize_processed_data(self):
        f, ax = plt.subplots(5,2, figsize=(8,10))
        f.tight_layout()
            
            #random_nums = random.sample(range(len(self.X_pair)), 5)
        for i in range(5):
                
            n = random.randint(0, len(self.X_pair))
            img0, img1 = self.X_pair[n]
            label = self.y_pair[n]       
            ax[i][0].imshow(img0)
            ax[i][0].set_title("Label: {}".format(label))
            ax[i][1].imshow(img1)
            ax[i][1].set_title("Label: {}".format(label))
            plt.show()
        
                
                
    def make_pairs(self):
         
        X= []
        y=[]
        labels = np.unique(self.y)
        label_to_idx = [np.where(self.y==label)[0] for label in labels]

   
        for i in tqdm(range(len(labels))):
            lbl1 = i
            label_ids = label_to_idx[i]
            for k in range(len(label_ids)) :
                img0 = self.X[label_ids[k]][0]
                        #img0 = np.asarray(img0).resize(105,105)
                for j in range(k+1, len(label_ids)):
                    img1 = self.X[label_ids[j]][0]
                            #img1 = np.asarray(img1).resize(105,105)
                    X.append([img0, img1])
                    y.append([1])
                
                    lbl2 = random.randint(0, len(labels)-1)
                    while(lbl2 == lbl1):
                        lbl2 = random.randint(0, len(labels)-1)
                    id = random.choice(label_to_idx[lbl2])
                    img2 = self.X[id][0]
                    X.append([img0, img2])
                    y.append([0])
        self.X_pair, self.y_pair = np.array(X), np.array(y)
        file_name = "{}_data.pkl".format("train" if self.train == True else "test")
        with open(file_name, "wb") as f:
            pkl.dump((self.X_pair, self.y_pair), f)
        print("Pickle file saved")
        


if __name__ == "__main__":
    
    train_dir = './images_background'
    print("> loading training data")
    print()
    data_obj = datainfo(train_dir, True)
    data_obj.load_details()
    data_obj.make_pairs()
    del data_obj
    

    test_dir = "./images_evaluation"
    data_obj = datainfo(test_dir, False)
    data_obj.load_details()
    data_obj.make_pairs()
    print(data_obj.n_classes)
    print(data_obj.n_alphabets)
    del data_obj
    
