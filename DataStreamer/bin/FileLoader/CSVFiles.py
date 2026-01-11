import pandas as pd


class CSVFiles:

    path = None
    file_holder = None

    def __init__(self, file_holder):
        self.file_holder = file_holder
        self.path = self.file_holder.file_path

    def load_file(self):

        f = pd.read_csv(self.path)

        eeg_column_name = []

        for i in f.columns:
            if 'eeg' in i.lower():
                eeg_column_name.append(i)

        eeg_data = f[eeg_column_name]
        del f

        self.file_holder.set_data(eeg_data.to_numpy())



