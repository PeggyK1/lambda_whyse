import pandas as pd
from sklearn.model_selection import train_test_split

class MyDataFrame(pd.DataFrame):
    def __init__(self, target, column):
        super().__init__()
        self.target = pd.Series
        self.column = "target"

class MyDataFrame(pd.DataFrame):
    def t_v_t_split(self, train, val, test):
