from domain.src.OnStartupCommand import OnStartupCommand
import ray

def run():
    command = OnStartupCommand()
    command.execute()
    command.destroy()


if __name__ == '__main__':
    ray.init(num_cpus=8,num_gpus=1)
    run()
