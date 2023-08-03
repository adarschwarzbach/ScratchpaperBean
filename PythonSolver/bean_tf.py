# TensorFlow implementation of the BEAN model
# Author: Adar Schwarzbach
import argparse
import os
import uuid


from pathlib import Path
import tensorflow as tf

F = 96500.0e0             # C / mol
met2lit = 1000.0e0
Rmu = 8.314e0
Temperature = 298.0e0
muH = 362e-9
muOH = 205e-9
visc = 1e-3  # Dynamic viscosity (water) (Pa s)


class BeanInit(tf.Module):
    def __init__(self):
        super(BeanInit, self).__init__()