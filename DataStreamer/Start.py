from DataStreamer.bin.FileLoader.CSVFiles import CSVFiles
from bin.UI.Top import MainUI
from bin.FileLoader.FileHolder import FileHolder
from bin.FileLoader.CSVFiles import CSVFiles
from bin.Streamer.StreamData import stream
from bin.FileLoader.BDFFiles import BDFReader
import os, sys

def start():
    fh = FileHolder()
    root = MainUI()
    root.set_file_holder(fh)
    root.mainloop()

    if os.path.splitext(fh.file_path)[1] == '.csv':
        CSVFiles(fh).load_file()
    elif os.path.splitext(fh.file_path)[1] == '.bdf':
        BDFReader(fh).load_file()
    else:
        print('File not supported')
        sys.exit()

    CSVFiles(fh).load_file()
    stream(fh).create_stream().stream_data()









if __name__ == '__main__':
    start()