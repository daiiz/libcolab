from google.colab import userdata
import os
import subprocess
import tempfile

def run_command(command):
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    return completed_process.stdout.decode("utf-8")  # return output as string


# deprecated
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


def get_audience2(colab_name):
    if not colab_name:
        return None
    aud_key = f"{colab_name}-client_id"
    aud = userdata.get(aud_key)

    cred_key = f"{colab_name}-cred"
    # cred_json = userdata.get(cred_key)

    # Write credential JSON to temporary file and activate service account
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
        tmp_file.write('{ "test": "data" }')
        key_file_path = tmp_file.name
        print(">", key_file_path)

    try:
        pass
        # run_command(
        #     " ".join(
        #         [
        #             "gcloud",
        #             "auth",
        #             "activate-service-account",
        #             "--key-file={}".format(key_file_path),
        #         ]
        #     )
        # )
    finally:
        os.unlink(key_file_path)

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
