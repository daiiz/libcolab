import subprocess


def run_command(command):
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    return completed_process.stdout.decode("utf-8")  # return output as string


def run_command(command):
    return os.system(command)


def sample5(msg):
    print(msg)
    print(run_command("ls -l"))
