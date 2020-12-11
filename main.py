import ray
# TODO: Move this out of here
import tensorflow as tf
from domain.src.OnStartupCommand import OnStartupCommand


def run():
    command = OnStartupCommand()
    command.execute()
    command.destroy()


if __name__ == '__main__':
    ray.init(num_cpus=8, num_gpus=1)

    with tf.device('/GPU:0'):
        run()
