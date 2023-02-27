import os
import pickle
import scipy
import datetime
import numpy as np
import tensorflow as tf

seed = 2
tf.random.set_seed(seed)
np.random.seed(seed)

import simclr_models
import simclr_utitlities

# Dataset-specific
# working_directory = 'SleepEEG/'
# data_folder = 'SleepEEG'

working_directory = 'MIMIC/'
data_folder = 'MIMIC'
model_name = '20230227-115713_finetuning.hdf5'

# Load preprocessed data
np_test = (np.load(os.path.join(data_folder, 'test_x.npy')),
           np.load(os.path.join(data_folder, 'test_y.npy')))

pretrained_model = tf.keras.models.load_model(os.path.join(working_directory, model_name), compile=False)

print(simclr_utitlities.evaluate_model_simple(pretrained_model.predict(np_test[0]), np_test[1], return_dict=True))