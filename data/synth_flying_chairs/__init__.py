#!/usr/bin/python2
# -*- coding:utf-8 -*-
# Created Time: Sun 17 Apr 2016 12:49:31 PM EDT
# Mail: hewr2010@gmail.com
import os
import cv2
import glob
import random
import itertools
import numpy as np

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def generate(prefix, randomize=False):
    gt_paths = glob.glob('%s/*.txt' % prefix)
    if randomize:
        rng = np.random.RandomState(9378)
        rng.shuffle(gt_paths)
    for gt_path in gt_paths:
        lpath = '%s.left.jpg' % (gt_path[:-4])
        rpath = '%s.right.jpg' % (gt_path[:-4])
        limg = cv2.imread(lpath)
        rimg = cv2.imread(rpath)
        gt = map(float, open(gt_path).readline().strip().split(' '))
        yield limg, rimg, gt

def size_of_train():
    return len(glob.glob(os.path.join(BASE_DIR, 'train/*.txt')))

def size_of_test():
    return len(glob.glob(os.path.join(BASE_DIR, 'val/*.txt')))

def size_of_dataset(train_or_test='train'):
    if train_or_test == 'train':
        return size_of_train()
    else:
        return size_of_test()

def trainset(randomize=False):
    return generate(os.path.join(BASE_DIR, 'train'), randomize=randomize)

def testset(randomize=False):
    return generate(os.path.join(BASE_DIR, 'val'), randomize=randomize)

def get_dataset(train_or_test='train', **kwargs):
    if train_or_test == 'train':
        return trainset(**kwargs)
    else:
        return testset(**kwargs)
