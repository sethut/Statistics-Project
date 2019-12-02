###매매가 변동 크기###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import deep_m
def run(arg_yesan,arg_month,arg_region):
	meme = pd.read_csv("meme.csv", encoding="utf-8")
	year=["2012년", "2013년" , "2014년","2015년", "2016년" , "2017년", "2018년" , "2019년"]
	region=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']
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
	
#for i in range(0,len(region_list)):
	meme_df.loc[0] = meme_money[region.index(arg_region)]
#meme_df.loc[i] = meme_money[i]
#	print(meme_df[arg_month])
	meme_mean=[]
	
	#### 연도별 평균 ### 
	for i in range(len(year_list)) :
			meme_mean.append(meme_df[year_list[i]].mean(axis=1))
	if arg_month > 95 :
		y,m = divmod(arg_month,12)
		year.append(str(y+2012)+"년" +str(m+1) + "월")
	#	meme_mean.append(arg_y)
	#print(arg_y)
	print(arg_month)
	### DataFrame 생성 ### 
	meme_2_df = pd.DataFrame(columns = year)
	for i in range(len(year)):
		meme_2_df[year[i]] = meme_mean[i]

	print(w_test.monthly_2_df)
#	if arg_month > 95 :
#		meme_2_df[arg_month]=arg_y
	### MatePlot 생성 ###
	plt.figure(figsize=(7,7))
	plt.title("building")
#	plt.text(50, .025, arg_y)	
	plt.grid(True)
	plt.plot(year,meme_mean,label=region_list)
	plt.plot(year[-1],meme_mean[-1],"xk")
	plt.text(year[-2],meme_mean[-1]+10000, str(round(meme_mean[-1],4)))
	plt.axhline(y=arg_yesan/1000, color='r', linewidth=4)
	plt.legend(region_list,loc = 'upper left',ncol=4,bbox_to_anchor=(1, 1)) 
	rc('font', family='NanumGothic')
	plt.rcParams['axes.unicode_minus'] = False
	plt.show()
#deep_m.run(arg_month,arg_region)




