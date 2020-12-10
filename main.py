from domain.src.OnStartupCommand import OnStartupCommand
import tensorflow as tf

import ray
import os


def run():
    command = OnStartupCommand()
    command.execute()
    command.destroy()


if __name__ == '__main__':
    ray.init(num_cpus=8,num_gpus=1)
    print("Num GPUs Available: ", tf.config.list_physical_devices())
    with tf.device('/GPU:0'):
        run()
