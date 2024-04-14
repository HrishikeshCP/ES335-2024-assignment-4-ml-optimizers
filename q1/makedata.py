# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
from random import shuffle

# create directories
dataset_home = 'q1/monkey_vs_rabbit_dataset/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	labeldirs = ['monkey/', 'rabbit/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)
# copy training dataset images into subdirectories
src_directory = 'q1/dataset/'

# Define the exact number of images for each set
num_train = 80
num_test = 20

# Counter variables for each class
monkey_train_count = 0
rabbit_train_count = 0

# Shuffle the list randomly
shuffle(listdir(src_directory))

# Iterate through the files and copy them to appropriate directories
for file in listdir(src_directory):
    src = src_directory + '/' + file
    if file.startswith('monkey'):
        if monkey_train_count < num_train:
            dst = dataset_home + 'train/monkey/' + file
            monkey_train_count += 1
        else:
            dst = dataset_home + 'test/monkey/' + file
    elif file.startswith('rabbit'):
        if rabbit_train_count < num_train:
            dst = dataset_home + 'train/rabbit/' + file
            rabbit_train_count += 1
        else:
            dst = dataset_home + 'test/rabbit/' + file
    copyfile(src, dst)