import platform
print('python version : ', platform.architecture())

import pandas as pd
path = r'C:\source\exercise\data\typhoon.csv'
path = path.replace('\\', '/')
print(path)
typhoon_df = pd.read_csv(path, encoding='cp949')
typhoon_df
typhoon_kor_df = typhoon_df.copy()
typhoon_asia_df = typhoon_df.copy()
split = lambda x : int(str(x).split('(')[0])
split_kor = lambda x : int(str(x).split('(')[1][0])
# typhoon_kor_df['1월'] = [split(i) for i in typhoon_df['1월'].values ]
typhoon_kor_df['1월'] = [split_kor(i) for i in typhoon_df['1월'].values ]
for i in typhoon_kor_df.columns:
    # print(i)
    typhoon_asia_df[i] = [split(i) for i in typhoon_df[i].values ]
    typhoon_kor_df[i] = [split_kor(i) for i in typhoon_df[i].values ]
# 태풍이 증가하고 있는가?
# typhoon_df
typhoon_kor_df