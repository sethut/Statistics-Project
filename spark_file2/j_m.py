###################연도별로 정리 버전################
### 매 전 추 ### 
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm

def run():
    ratio = pd.read_csv("meme-jeonse.csv", encoding="utf-8")
    year=["2012년", "2013년" , "2014년" , "2015년", "2016년" , "2017년", "2018년" , "2019년"]

    date=list(ratio)
    date_list=date[0:]
    year_list=[] 

    for i in range(len(year)) :
        year_list.append([dec for dec in date_list if year[i] in dec])


    region_list=ratio['지 역'].values
    ratio_money=[]
    for i in range(0,len(region_list)):
        ratio_money.append(ratio.iloc[i].values[0:])

    ### DataFrame 생성 ### 
    ratio_df = pd.DataFrame(columns = date_list)

    for i in range(0,len(region_list)):
        ratio_df.loc[i] = ratio_money[i]

    ratio_mean=[]

    #### 연도별 평균 ### 
    for i in range(len(year_list)) :
        ratio_mean.append(ratio_df[year_list[i]].mean(axis=1))
    
    ### DataFrame 생성 ### 
    ratio_2_df = pd.DataFrame(columns = year)
    for i in range(len(year)):
        ratio_2_df[year[i]] = ratio_mean[i]

    ### plot 생성 ### 
    remainder_ratio=100-ratio_mean[5]
    plt.figure(figsize=(20,20))
    plt.bar(region_list, ratio_mean[5], width=0.5,color='b')
    plt.bar(region_list, remainder_ratio, width=0.5, bottom=ratio_mean[5],color='r')
    plt.show()


