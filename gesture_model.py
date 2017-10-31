from __future__ import print_function
import tensorflow as tf
import helpers as hp
from data_pipeline import DataPipeline

class GestureRecognizer:

    def __init__(self, configuration):

        self.conf = configuration
        self.data_pipeline = DataPipeline(self.conf.batch_size, self.conf.max_memory)
        self.input_size = self.conf.data_pipeline.get_input_size
        self.output_size = self.data_pipeline.get_output_size()
        self.lstm = tf.contrib.rnn.BasicLSTMCell(self.conf.state_size)
        self.weights = hp.weight_variables([self.conf.state_size,self.output_size])
        self.biases = hp.bias_variables([self.output_size])

        self.input = tf.placeholder(tf.float32, shape=[self.conf.batch_size,
                                                               self.conf.max_memory,
                                                               self.input_size])
        self.initial_state = tf.placeholder(tf.float32, shape=[self.conf.batch_size,
                                                                self.conf.state_size])
        self.current_state = tf.placeholder(tf.float32, shape=[self.conf.batch_size,
                                                                self.conf.state_size])
        self.hidden_state = tf.placeholder(tf.float32, shape=[self.conf.batch_size,
                                                               self.conf.state_size])
        self.label = tf.placeholder(tf.int32, shape=[self.conf.batch_size, self.conf.max_memory])

        self.zero_state = self.lstm.zero_state(batch_size=self.conf.batch_size, dtype=tf.float32)


    def train(self):
        for batch in self.input:
            output,  = self.lstm(batch, )  #batch: max_mem X input_size







