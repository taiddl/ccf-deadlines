import os


def merge_conferences() -> None:
    sub_folders: list[os.DirEntry] = [f for f in os.scandir("../conference") if f.is_dir()]
    sub_folder: os.DirEntry
    yml_files: list[str] = []
    for sub_folder in sub_folders:
        dir_path: str
        file_names: list[str]
        for (dir_path, _, file_names) in os.walk(sub_folder):
            break
        for file_name in file_names:
            yml_files.append(dir_path.replace("\\", "/") + "/" + file_name)
    data: str = ""
    for yml_file in yml_files:
        if yml_file.endswith(".yml"):
            with open(file=yml_file, mode="r", encoding="utf-8") as yml:
                yml_content = yml.read()
                if not yml_content.endswith("\n"):
                    yml_content += "\n"
                data += yml_content
    with open("../conference/all_conf.yml", mode="w", encoding="utf-8") as all_conf:
        all_conf.write(data)


if __name__ == '__main__':
    merge_conferences()
    print(r"succeed!")
