import subprocess


def run_command(command):
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    return completed_process.stdout.decode("utf-8")  # return output as string


def get_audience(drive_root_name, colab_name):
    base_dir = "/content/drive/MyDrive/{0}/{1}".format(drive_root_name, colab_name)
    key_file_path = "{0}/cred.json".format(base_dir)
    aud = ""
    with open("{0}/client_id.txt".format(base_dir), "r") as fp:
        aud = fp.readline()

    run_command(
        " ".join(
            [
                "gcloud",
                "auth",
                "activate-service-account",
                "--key-file={}".format(key_file_path),
            ]
        )
    )

    return aud.strip()


def get_token(audience):
    token = run_command(
        " ".join(
            [
                "gcloud",
                "auth",
                "print-identity-token",
                "--audiences={}".format(audience),
            ]
        )
    )
    return token.strip()
