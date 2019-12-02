##################연도별로 정리 버전################
### 월 추 ###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn import linear_model
def run(arg_yesan,arg_month,arg_region):
	Arg_month=arg_month-41
	bojeungum = pd.read_csv("bojeungum.csv", encoding="utf-8")
	year=["2015년", "2016년" , "2017년", "2018년" , "2019년"]
	region=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']
	date=list(bojeungum)
	date_list=date[0:]
	year_list=[] 
	region_list=bojeungum['지 역'].values
	bojeungum_money=[]
	for i in range(0,len(region_list)):
	    bojeungum_money.append(bojeungum.iloc[i].values[0:])

	a=[]
	for i in range(1,len(date_list)):
	    a.append(i)
	df = pd.DataFrame({
		'month' : a,
		'bojeungum' : bojeungum.loc[region.index(arg_region)][1:]
	})

	X = df.loc[:,['month']]
	y = df.loc[:,['bojeungum']]
	print(y)
	
	reg = linear_model.LinearRegression()
	reg.fit(X,y)
	print("x=",X)
	print("y=",y)
	print( "R²=", reg.score(X,y) )
	print( "coefficient=", reg.coef_ )
	print( "intercept=", reg.intercept_ )
	
	for i in range(len(year)) :
		year_list.append([dec for dec in date_list if year[i] in dec])

	region_list=bojeungum['지 역'].values

	wolse_money=[]
	for i in range(0,len(region_list)):
		wolse_money.append(bojeungum.iloc[i].values[0:])
	
	### DataFrame 생성 ### 
	bojeungum_df = pd.DataFrame(columns = date_list)
	
	bojeungum_df.loc[0] = wolse_money[region.index(arg_region)]
	bojeungum_mean=[]

	#### 연도별 평균 ### 
	for i in range(len(year_list)) :
			bojeungum_mean.append(bojeungum_df[year_list[i]].mean(axis=1))
	if Arg_month > 52 :
	        y,m = divmod(arg_month,12)
	        year.append(str(y+2012)+"년" +str(m+1) + "월")
	        bojeungum_mean.append(reg.coef_[0][0] * Arg_month + reg.intercept_[0])
	### DataFrame 생성 ### 
	bojeungum_2_df = pd.DataFrame(columns = year)
	for i in range(len(year)):
		bojeungum_2_df[year[i]] = bojeungum_mean[i]

	plt.figure(figsize=(8,8))
	plt.title('BJ.py')
	plt.grid(True)
	plt.plot(year,bojeungum_mean)
	plt.plot(year[-1],bojeungum_mean[-1],"xk")
	plt.text(year[-2],bojeungum_mean[-1]+10000, str(round(bojeungum_mean[-1],4)))
	plt.legend(arg_region,loc = 'upper left',ncol=4,bbox_to_anchor=(1, 1))
	print("!!!!!!!!!!",arg_region) 
	rc('font', family='NanumGothic')
	plt.rcParams['axes.unicode_minus'] = False
	plt.show()

