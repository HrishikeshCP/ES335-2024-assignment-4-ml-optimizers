# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
# create directories
dataset_home = 'q1/monkey_vs_rabbit_dataset/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	labeldirs = ['monkey/', 'rabbit/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)
# seed random number generator
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.25
# copy training dataset images into subdirectories
src_directory = 'q1/dataset/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	dst_dir = 'train/'
	print(file)
	if random() < val_ratio:
		dst_dir = 'test/'
	if file.startswith('monkey'):
		dst = dataset_home + dst_dir + 'monkey/'  + file
		copyfile(src, dst)
	elif file.startswith('rabbit'):
		dst = dataset_home + dst_dir + 'rabbit/'  + file
		copyfile(src, dst)