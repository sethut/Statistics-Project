###################연도별로 정리 버전################
### 월 추 ###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def run():
	monthly = pd.read_csv("wolse.csv", encoding="utf-8")
	year=["2015년", "2016년" , "2017년", "2018년" , "2019년"]

	date=list(monthly)
	date_list=date[0:]
	year_list=[] 

	for i in range(len(year)) :
	    year_list.append([dec for dec in date_list if year[i] in dec])

	region_list=monthly['지 역'].values
	monthly_money=[]
	for i in range(0,len(region_list)):
	    monthly_money.append(monthly.iloc[i].values[0:])

	### DataFrame 생성 ###
	monthly_df = pd.DataFrame(columns = date_list)

	for i in range(0,len(region_list)):
	     monthly_df.loc[i] = monthly_money[i]

	monthly_mean=[]

	#### 연도별 평균 ###
	for i in range(len(year_list)) :
	     monthly_mean.append(monthly_df[year_list[i]].mean(axis=1))

     

	### DataFrame 생성 ###
	monthly_2_df = pd.DataFrame(columns = year)
	for i in range(len(year)):
	    monthly_2_df[year[i]] = monthly_mean[i]

	### MatePlot 생성 ###
	plt.figure(figsize=(7,7))
	plt.plot(year,monthly_mean,label=region_list)
	plt.legend(region_list,loc = 'upper left',ncol=4,bbox_to_anchor=(1, 1))
	rc('font', family='AppleGothic')
	plt.rcParams['axes.unicode_minus'] = False
	plt.show()
