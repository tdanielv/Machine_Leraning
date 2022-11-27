import pandas as pd
import numpy as np
from numpy import NaN
from sklearn import preprocessing

dataframe = pd.DataFrame({
    'Chupa-Chups': [3, 5, 4, 5],
    'Doshirak': [4, 5, 3, 4],
    'Boyarishnik': [5, 5, 3, 3],
    'VAZ': [3, 4, 2, 3],
    'Semechki': [4, 3, 5, NaN]},
index=['Vasya', 'Petya', 'Masha', 'Sasha'])

def by_feature(df, object, feauture):
    KK_before = df.corr()[feauture]
    KK = KK_before[KK_before.index != feauture]

    avg_before = df[df.index != object].mean(axis=0)
    avg = avg_before[avg_before.index != feauture]

    all_feature_known = df.loc[object][df.loc[object].index != feauture]
    KK_known_avg = ((all_feature_known - avg) * KK).sum()
    avg_feature_unknown = df[feauture].mean()
    P_A = avg_feature_unknown + 1 / KK.abs().sum() * KK_known_avg
    return P_A

object = 'Sasha'
feature = 'Semechki'
print(by_feature(dataframe, object, feature))