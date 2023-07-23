import os


def run_command(command):
    return os.system(command)


def sample3(msg):
    print(msg)
    run_command("ls -l")
