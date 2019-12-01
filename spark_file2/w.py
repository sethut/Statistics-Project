###################연도별로 정리 버전################
### 월 추 ###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn import linear_model
def run(arg_yesan,Arg_month,arg_region):
	Arg_month=Arg_month-41
	monthly = pd.read_csv("wolse.csv", encoding="utf-8")
	year=["2015년", "2016년" , "2017년", "2018년" , "2019년"]
	date=list(monthly)
	date_list=date[0:]
	year_list=[] 

	region_list=monthly['지 역'].values
	region=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']
	monthly_money=[]
	for i in range(0,len(region_list)):
	    monthly_money.append(monthly.iloc[i].values[0:])

	a=[]
	for i in range(1,len(date_list)):
	    a.append(i)
	df = pd.DataFrame({
		'month' : a,
		'wolse' : monthly.loc[region.index(arg_region)][1:]
	})

	X = df.loc[:,['month']]
	y = df.loc[:,['wolse']]
	print(y)
	
	reg = linear_model.LinearRegression()
	reg.fit(X,y)
	print("x=",X)
	print("y=",y)
	print( "R²=", reg.score(X,y) )
	print( "coefficient=", reg.coef_ )
	print( "intercept=", reg.intercept_ )
	new_y=[]
	#for i in range(0,len(a)):
	#    new_y.append(reg.coef_ * a[i] + reg.intercept_)
	for i in range(0,len(date_list)-1):
	 	new_y.append(df['wolse'][i])

	deep_x=[]
	deep_y=[]
	for i in range(0,Arg_month):
	    deep_x.append(i)

	#for i in range(0,Arg_month):
	#    deep_y.append(reg.coef_[0][0] * deep_x[i] + reg.intercept_[0])
	a.append(Arg_month)
	print(a)
	new_y.append(reg.coef_[0][0] * deep_x[Arg_month-1] + reg.intercept_[0])

	print(deep_y)
	### MatePlot 생성 ###
	plt.figure(figsize=(7,7))
	plt.title("wolse")
	plt.grid(True)
	plt.plot(a,new_y,label=year)
	plt.plot(a[-1],new_y[-1],"xk")
	plt.text(a[-1]-2,new_y[-1]+5, str(new_y[-1]))
	plt.legend(region_list,loc = 'upper left',ncol=4,bbox_to_anchor=(1, 1))
	rc('font', family='NanumGothic')
	plt.rcParams['axes.unicode_minus'] = False
	plt.show()
