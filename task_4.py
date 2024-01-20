import datetime
import os
import subprocess


def remove_files(path: str, days: int) -> None:
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if datetime.datetime.now() - file_time > datetime.timedelta(days=days):
                os.remove(file_path)
                print(f"File {file} removed")


if __name__ == "__main__":
    ###
    some_dir = "./some_dir"
    if not os.path.isdir(some_dir):
        os.mkdir(some_dir)
    for d in range(1, 10):
        file_old = (datetime.datetime.now() - datetime.timedelta(days=d)).strftime(
            "%Y%m%d%H%M"
        )
        file_name = f"{d}_old.txt"
        file_path = os.path.join(some_dir, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("Some content")
            subprocess.run(["touch", "-t", file_old, file_path])
            print(f"File {file_name} created")
        else:
            print(f"File {file_name} already exists")

    ### If you are not using MacOS, comment out the part of the code below before ###
    remove_files(some_dir, 10)
