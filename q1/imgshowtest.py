
# load and confirm the shape
from numpy import load
photos = load('q1\monkey_vs_rabbit_photos.npy')
labels = load('monkey_vs_rabbit_labels.npy')
print(photos.shape, labels.shape)