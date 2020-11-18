import numpy as np
import torch
import pandas as pd
from numpy.random import randn
import plotly.express as px

np.random.seed(101)
csv_file = '/Users/sylvainmougel/OneDrive/Stash evolution.csv'
def test1():
    rand_mat = randn(5,4)
    df = pd.DataFrame(rand_mat, index='a b c d e'.split(), columns='w x y z'.split())
    print(df[['w', 'x']])
    print(torch.__version__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv(csv_file)
    df.columns()
    # filter out nan value
    filtered = df[~(pd.isnull(df['Total Invested']))]
    print(df)
    #print(torch.randint(5,10, (2,4,2)))


