import pandas as pd

class Dataset:
    def __init__(self, name):
        self.data = pd.read_csv('datasets/' + name + '.csv')

    def getData(self):
        return self.data.to_numpy()