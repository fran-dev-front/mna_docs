import numpy as np
import random

class GenerateImageBatch:

    def __init__(self, img,
                 lab,
                 batch_size):

        self.img_h = img.shape[1]
        self.img_w = img.shape[2]
        self.img_count = img.shape[0]
        self.batch_size = batch_size
        self.imgs = img
        self.labs = lab
        self.n = img.shape[0]
        self.indices = list(range(self.n))
        self.cur_index = 0
        self.inputs = None
        self.outputs = None

    ''' Next sample'''
    def next_sample(self):
        self.cur_index += 1
        if self.cur_index >= self.n:
            self.cur_index = 0
            random.shuffle(self.indices)
        return self.imgs[self.indices[self.cur_index]], self.labs[self.indices[self.cur_index]]

    ''' Create next batch of images and labels to feed the NN'''
    def next_batch(self):

        X_data = np.zeros([self.batch_size, self.img_w, self.img_h, 1])
        Y_data = np.zeros([self.batch_size, self.img_w, self.img_h, 1])

        for i in range(self.batch_size):
            img, lab = self.next_sample()
            img = img.T
            img = np.expand_dims(img, -1)
            X_data[i] = img
            lab = lab.T
            lab = np.expand_dims(lab, -1)
            Y_data[i] = lab

        inputs = X_data
        outputs = Y_data
        self.inputs = inputs
        self.outputs = outputs