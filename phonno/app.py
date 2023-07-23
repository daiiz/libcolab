import os


def run_command(command):
    return os.system(command)


def sample4(msg):
    print(msg)
    print(run_command("ls -l"))
