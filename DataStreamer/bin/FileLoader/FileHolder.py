import numpy


class FileHolder:
    file_path = None
    data = None
    repeat = None
    fs = None

    def __init__(self):
        pass


    def set_file_path(self, file_path:str):
        self.file_path = file_path

    def set_data(self, data:numpy.ndarray):
        self.data = data

    def set_repeat(self, repeat:bool):
        self.repeat = repeat

    def set_fs(self, fs:int):
        self.fs = fs