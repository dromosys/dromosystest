import os
import pandas as pd


def print_hello_world():
    print("Hello World")


def get_csv():
    this_path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(os.path.join(this_path, 'test.csv'))
    return df

