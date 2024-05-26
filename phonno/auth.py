import lib.auth as auth


def get_audience(drive_root_name, colab_name):
    return auth.get_audience(drive_root_name, colab_name)


def get_token(audience):
    return auth.get_token(audience)
