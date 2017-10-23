from __future__ import print_function
import tensorflow as tf
import helpers as hp
from data_pipeline import DataPipeline

class GestureRecognizer:

    def __init__(self, configuration):
        self.conf = configuration
        self.data_pipeline = DataPipeline(self.conf.batch_size, self.conf.max_memory)
        self.initial_state = tf.placeholder(tf.float32, shape=[self.conf.batch_size,self.conf])
