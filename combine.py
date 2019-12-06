import pandas as pd
import numpy as np


filepath = '/Users/hfeiss/dsi/case-study/pandas-eda-case-study/data/youtube-new/'

ca = pd.read_csv(filepath + 'CAvideos.csv', sep=',')
ca['country_code'] = 'ca'
de = pd.read_csv(filepath + 'DEvideos.csv', sep=',')
de['country_code'] = 'de'
fr = pd.read_csv(filepath + 'FRvideos.csv', sep=',')
fr['country_code'] = 'fr'
gb = pd.read_csv(filepath + 'GBvideos.csv', sep=',')
gb['country_code'] = 'gb'
ia = pd.read_csv(filepath + 'INvideos.csv', sep=',')
ia['country_code'] = 'ia'
jp = pd.read_csv(filepath + 'JPvideos.csv', sep=',', encoding='latin-1')
jp['country_code'] = 'jp'
kr = pd.read_csv(filepath + 'KRvideos.csv', sep=',', encoding='latin-1')
kr['country_code'] = 'kr'
ru = pd.read_csv(filepath + 'RUvideos.csv', sep=',', encoding='latin-1')
ru['country_code'] = 'ru'
mx = pd.read_csv(filepath + 'MXvideos.csv', sep=',', encoding='latin-1')
mx['country_code'] = 'mx'
us = pd.read_csv(filepath + 'USvideos.csv', sep=',')
us['country_code'] = 'us'


#everything = pd.DataFrame()
everything = pd.concat([ca, de, fr, gb, ia, jp, kr, ru, mx, us])


if __name__ == '__main__':
    print(everything.columns)