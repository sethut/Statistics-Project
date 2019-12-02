###매매가 변동 크기###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def run() :
	rc('font', family='NanumGothic')
	meme = pd.read_csv("meme.csv", encoding="utf-8")
	year=["2012년", "2013년" , "2014년","2015년", "2016년" , "2017년", "2018년" , "2019년"]

	date=list(meme)
	date_list=date[0:]
	year_list=[] 

	for i in range(len(year)) :
	    year_list.append([dec for dec in date_list if year[i] in dec])

	region_list=meme['지 역'].values
	meme_money=[]
	for i in range(0,len(region_list)):
	    meme_money.append(meme.iloc[i].values[0:])

	### DataFrame 생성 ### 
	meme_df = pd.DataFrame(columns = date_list)

	for i in range(0,len(region_list)):
	     meme_df.loc[i] = meme_money[i]

	meme_mean=[]

#### 연도별 평균 ### 
	for i in range(len(year_list)) :
	     meme_mean.append(meme_df[year_list[i]].mean(axis=1))

    

	### DataFrame 생성 ### 
	meme_2_df = pd.DataFrame(columns = year)
	for i in range(len(year)):
	    meme_2_df[year[i]] = meme_mean[i]

	### MatePlot 생성 ### 
	plt.figure(figsize=(10,7))
	plt.grid(True)
	plt.plot(year,meme_mean,label=region_list)
	plt.legend(region_list,loc = 'upper left',ncol=4,bbox_to_anchor=(1, 1)) 
	plt.rcParams['axes.unicode_minus'] = False

	plt.show()
