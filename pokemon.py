import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon1gen.csv')
#print(df.iloc[1:3])
#iloc is rows then columns (:,:)

df_sorted = df.sort_values(['Combat Power', 'Speed', 'Attack', 'Defense'], ascending=[False, False, False, False])

print(df_sorted)