
from os import chdir, listdir, mkdir, getcwd
from pathlib import Path

__all__ = ['sort_files']


def sort_files(directory: str | Path = "test_dir"):
    chdir(directory)
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        file.replace(f'{ext.upper()}\\{file.name}')

sort_files()


if __name__ == '__main__':
    sort_files()
