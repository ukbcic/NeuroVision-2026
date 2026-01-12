
from mne.io import read_raw_bdf


class BDFReader:

    path = None
    file_holder = None

    def __init__(self, file_holder):
        self.file_holder = file_holder
        self.path = self.file_holder.file_path

    def load_file(self):

        raw = read_raw_bdf(self.path).to_data_frame()

        eeg_column_name = []

        for i in raw.columns:
            if 'eeg' in i.lower():
                eeg_column_name.append(i)

        eeg_data = raw[eeg_column_name]
        del raw

        self.file_holder.set_data(eeg_data.to_numpy())


