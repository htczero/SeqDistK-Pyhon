import os


class File:
    def __init__(self, file_path: str):
        self.directory, name = os.path.split(file_path)
        self.name, self.ext = os.path.splitext(name)
        self.full_path = file_path  # type: str
        self.name_with_extension = self.name + self.ext  # type:str
        _, self.directory_name = os.path.split(self.directory)  # type:str

    @staticmethod
    def recurrence_load(dir_path: str):
        dirs = []

        def _rec_load(path: str):
            tmps = os.listdir(path)
            p = os.path.join(path, tmps[0])
            if os.path.isfile(p):
                dirs.append(path)
            elif os.path.isdir(p):
                [_rec_load(os.path.join(path, sub_path)) for sub_path in tmps]
            else:
                return

        _rec_load(dir_path)
        return dirs

    @staticmethod
    def get_file_path(dir_path: str):
        tmps = os.listdir(dir_path)
        return [File(os.path.join(dir_path, sub_path)) for sub_path in tmps]
