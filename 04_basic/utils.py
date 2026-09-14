import os


def get_files(out_dir):
    if not os.path.exists(out_dir):
        return []

    return os.listdir(out_dir)


def save_file(out_dir, filename, content):
    os.makedirs(out_dir, exist_ok=True)

    file_path = os.path.join(out_dir, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path