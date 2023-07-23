import subprocess


def run_command(command):
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    return completed_process.stdout.decode("utf-8")  # return output as string


def sample5(msg):
    print(msg)
    print(run_command("ls -l"))


def get_token(drive_root_name, colab_name):
    base_dir = "/content/drive/MyDrive/{0}/{1}".format(drive_root_name, colab_name)
    key_file_path = "{0}/cred.json".format(base_dir)
    aud = ""
    with open("{0}/client_id.txt".format(base_dir), "r") as fp:
        aud = fp.readline()

    res = run_command(
        " ".join(
            [
                "gcloud",
                "auth",
                "activate-service-account",
                "--key-file={}".fromat(key_file_path),
            ]
        )
    )
    print(res)

    print("aud:", aud)
