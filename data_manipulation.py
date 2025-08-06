import pandas as pd


directory = "C:/Users/mohammad.ghasempour/Documents/cursor/jadi/Data/USA_Major_Cities.csv"
my_file = pd.read_csv(directory)


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

print(my_file.describe())

