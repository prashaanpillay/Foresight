from domain.src.OnStartupCommand import OnStartupCommand


def run():
    command = OnStartupCommand()
    command.execute()
    command.destroy()


if __name__ == '__main__':
    run()
