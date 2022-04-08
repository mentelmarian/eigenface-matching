#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:08:23 2022

@author: 
    Marian Leonard Mentel
"""

import os
import math

# return all images contained in "folder" of the specified size
def get_all_eigenface(folder, size):
    files = os.listdir('eigenfaces/'+str(size)+'/'+folder)
    files_path = []
    for i in files:
        temp = 'eigenfaces/'+str(size)+'/'+folder + '/' + i
        files_path.append(temp)
        files_path.sort()
    return files_path

# returns the eigenface contained in "filename"
def read_from_file_eigenface(filename):
    eigenfaces = []
    f = open(filename)
    temp = f.readline()
    aux = temp.split(',')
    eigenfaces = []
    for elem in aux:
        eigenfaces.append(int(elem))
    return eigenfaces

# compute the squared euclidean distance 
def squared_euclidean_distance(vector_1, vector_2):
    distance = 0
    for i in range(len(vector_1)):
        distance += math.pow(vector_1[i]-vector_2[i], 2)
    return distance

# returns the image's person ID (for CASIA_1__0_3.txt returns 0)
def get_eigenface_class(filename):
    name = filename.split('/')
    tmp = name[len(name)-1]
    label = tmp.split('.')
    return label[0].split('_')[3]