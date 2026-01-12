import time

from ..FileLoader.FileHolder import FileHolder
import pylsl
from pylsl import StreamInfo, StreamOutlet, resolve_streams
import time

class stream():

    repeat = None
    data = None
    outlet = None
    frequency = None
    stream_name = None



    def __init__(self, FileHolder):
        self.data = FileHolder.data
        self.repeat = FileHolder.repeat
        self.frequency = FileHolder.fs
        self.stream_name = FileHolder.LSL_stream_name

    def create_stream(self):
        info = StreamInfo(self.stream_name, 'EEG', channel_count=self.data.shape[1],
                        channel_format=pylsl.cf_float32, source_id=f'stream_{time.time()}')

        self.outlet = StreamOutlet(info)

        return self

    def stream_data(self):

        for i in range(self.data.shape[0]):
            time.sleep(1/self.frequency)
            self.outlet.push_sample(self.data[i, :])
            print(self.data[i, :].tolist(), end='\r')

        if self.repeat:
            self.stream_data()
