from DataStreamer.bin.FileLoader.CSVFiles import CSVFiles
from bin.UI.Top import MainUI
from bin.FileLoader.FileHolder import FileHolder
from bin.FileLoader.CSVFiles import CSVFiles
from bin.Streamer.StreamData import stream

def start():
    fh = FileHolder()
    root = MainUI()
    root.set_file_holder(fh)
    root.mainloop()
    CSVFiles(fh).load_file()
    stream(fh).create_stream().stream_data()









if __name__ == '__main__':
    start()