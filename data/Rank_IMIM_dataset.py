import os.path
import random
import cv2
import numpy as np
import torch
import torch.utils.data as data
import data.util as util
from itertools import combinations
from scipy.special import comb


class RANK_IMIM_Dataset(data.Dataset):
    '''
    Read LR and HR image pair.
    If only HR image is provided, generate LR image on-the-fly.
    The pair is ensured by 'sorted' function, so please check the name convention.
    '''

    def name(self):
        return 'RANK_IMIM_Dataset'

    def __init__(self, opt,is_train):
        super(RANK_IMIM_Dataset, self).__init__()
        self.opt = opt
        self.paths_img = None
        self.LR_env = None # environment for lmdb
        self.HR_env = None
        self.is_train = is_train

        
        # read image list from lmdb or image files
        self.HR_env, self.paths_img = util.get_image_paths(opt['data_type'], opt['dataroot_HR'])
        # self.img_env1, self.paths_img1 = util.get_image_paths(opt['data_type'], opt['dataroot_img1'])

        self.label_path = opt['dataroot_label_file']
        
        # get image label scores
        self.label = {}
        f = open(self.label_path,'r')
        for line in f.readlines():
            line = line.strip().split()            
            self.label[line[0]] = line[1]
        f.close()
        self.combine = list(combinations([i for i in range(len(self.paths_img))], 2))

        assert self.paths_img, 'Error: img paths are empty.'
        

        # self.random_scale_list = [1, 0.9, 0.8, 0.7, 0.6, 0.5]
        self.random_scale_list = None

    def __getitem__(self, index):
        HR_path, LR_path = None, None
        img2 = None
        img2_path = None
        img2_score = None
        
        scale = self.opt['scale']
        HR_size = self.opt['HR_size']
        
        #print('index',index)
        if self.is_train:
            # get img1 and img1 label score      
            img1_index = self.combine[index][0]
            img1_path = self.paths_img[img1_index]
            img1 = util.read_img(self.HR_env, img1_path)
       
            img1_name = img1_path.split('/')[-1]
            img1_score = np.array(float(self.label[img1_name]),dtype='float')
            img1_score = img1_score.reshape(1)
        
            if img1.shape[2] == 3:
                img1 = img1[:, :, [2, 1, 0]]
            img1 = torch.from_numpy(np.ascontiguousarray(np.transpose(img1, (2, 0, 1)))).float()
            img1_score = torch.from_numpy(img1_score).float()
        
        
            # get img2 and img2 label score      
            img2_index = self.combine[index][1]
            img2_path = self.paths_img[img2_index]
            img2 = util.read_img(self.HR_env, img2_path)
       
            img2_name = img2_path.split('/')[-1]
            img2_score = np.array(float(self.label[img2_name]),dtype='float')
            img2_score = img2_score.reshape(1)
        
            if img2.shape[2] == 3:
                img2 = img2[:, :, [2, 1, 0]]
            img2 = torch.from_numpy(np.ascontiguousarray(np.transpose(img2, (2, 0, 1)))).float()
            img2_score = torch.from_numpy(img2_score).float()
            
            #print('img1:'+img1_name,' & ','img2:'+img2_name)
        
        else:
            # get img1      
            img1_path = self.paths_img[index]
            img1 = util.read_img(self.HR_env, img1_path)
       
            img1_name = img1_path.split('/')[-1]
            img1_score = np.array(float(self.label[img1_name]),dtype='float')
            img1_score = img1_score.reshape(1)
        
            if img1.shape[2] == 3:
                img1 = img1[:, :, [2, 1, 0]]
            img1 = torch.from_numpy(np.ascontiguousarray(np.transpose(img1, (2, 0, 1)))).float()
            img1_score = torch.from_numpy(img1_score).float()
            #print('img1:'+img1_name)
            
            
            # not useful
            img2_path = img1_path
            img2 = img1
            img2_score = img1_score

        
        '''
        import matplotlib.pyplot as plt
        plt.imshow(img1)
        plt.show()
        
        '''

        
        return {'img1': img1, 'img2': img2, 'img1_path': img1_path, 'img2_path': img2_path, 'score1':img1_score, 'score2':img2_score}

    def __len__(self):
        if self.is_train:
            length = comb(len(self.paths_img),2)
            return int(length)
        else:
            return len(self.paths_img)
