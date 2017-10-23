from __future__ import print_function
import tensorflow as tf
import time
import webbrowser
from subprocess import Popen, PIPE
import os


class Configuration:
    def __init__(self, train_log_path = './train', epochs=200, batch_size=100, max_memory=100):
        self.train_log_path = train_log_path
        self.epochs = epochs
        self.batch_size = batch_size
        self.max_memory = max_memory


def log_step(step, total_steps, start_time, error):
    progress = int(step / float(total_steps) * 100)
    seconds = time.time() - start_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print('%d%%\t|\t%d hours, %d minutes, %d seconds\t|\tStep: %d/%d\t\tError: %f' %
          (progress, int(h), int(m), int(s), step, total_steps, error))


def log_epoch(epoch, total_epochs, error):
    print('Epoch %d completed out of %d\nError: %f\n' %
          (epoch, total_epochs, error))


def weight_variables(shape, stddev=0.1, name='weights'):
    initial = tf.truncated_normal_initializer(stddev=stddev)
    return tf.get_variable(name, shape=shape,
                           initializer=initial)


def bias_variables(shape, value=0.1, name='biases'):
    initial = tf.constant_initializer(value)
    return tf.get_variable(name, shape=shape,
                           initializer=initial)


def open_tensorboard(train_log_path):
    tensorboard = Popen(['tensorboard', '--logdir=' + train_log_path],
                        stdout=PIPE, stderr=PIPE)
    time.sleep(5)
    webbrowser.open('http://0.0.0.0:6006')
    while input('Press <q> to quit') != 'q':
        continue
    tensorboard.terminate()
