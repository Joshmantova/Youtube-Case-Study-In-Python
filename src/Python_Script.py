from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

files = ['CA','DE','FR','GB','IN','JP','KR','MX','RU','US']
list = []

for file in files:
    filepath = "/Users/bechis/dsi/repo/CaseStudy/pandas-eda-case-study/data/youtube-new/"
    df1 = pd.read_csv(filepath+file+'videos.csv', encoding = 'latin-1')
    df1['Country_Code'] = '{}'.format(file)
    list.append(df1)

All_csv = pd.concat(list, sort='False')
All_csv = All_csv[['Country_Code','views']].groupby(All_csv['Country_Code']).agg({'views':'sum'})

if __name__=="__main__":
    print(All_csv.head())
    ax1 = plt.subplot(1,1,1)
    All_csv['views'].plot.pie()
    ax1.set_title("Views Per Country")
    plt.show()
