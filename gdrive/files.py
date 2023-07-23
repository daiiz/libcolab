def load_single_text(file_path, root_dir_name="MyDrive"):
    if not file_path:
        raise ValueError("file_path is required")
    with open("/content/drive/{}/{}".format(root_dir_name, file_path), "r") as fp:
        line = fp.readlines()[0].strip()
        return line
