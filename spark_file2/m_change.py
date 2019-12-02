###매매가 변동 크기###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import map2
def run(arg_month):
	rc('font', family='NanumGothic')
	meme = pd.read_csv("meme_change.csv", encoding="utf-8")
	date=list(meme)
	date_list=date[1:]
	region=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']

	current_increase=[178186.75, 195022 ,40445.5,33227,49081,123129,102768,59371,34547,172333,34972,17984.5,14926,35582]
	#ratio_col=set(ratio.iloc[1].values)
	meme_list=meme['지 역'].values
	meme_money=[]
	for i in range(0,len(meme_list)):
		meme_money.append(meme.iloc[i].values[1:])
	   

	year_list=list(meme)
	

	a=[]
	rslt=[]
	for i in range(1,len(year_list)):
	    a.append(i)

	### DataFrame 생성 ###
	meme_df = pd.DataFrame(index = date_list) 
	for i in range(0,len(meme_list)):
		meme_df[meme_list[i]]=meme.loc[i]
	
	meme_df['month']=a
	for i in range(len(region)):
	    x = meme_df.loc[:,["month"]]
	    y = meme_df.loc[:,[region[i]]]
	    from sklearn import linear_model
	    reg = linear_model.LinearRegression()
	    reg.fit(x,y)
	    print( "R²=", reg.score(x,y) )
	    print( "coefficient=", reg.coef_ )
	    print( "intercept=", reg.intercept_ )
	    print( region[i] , " : ", arg_month*reg.coef_[0][0] + reg.intercept_[0])
	    rslt.append(arg_month*reg.coef_[0][0] + reg.intercept_[0]-current_increase[i])
	### MatePlot 생성 ### 
	plt.figure(figsize=(7,7))
	plt.bar(region,rslt)
	plt.rcParams['axes.unicode_minus'] = False

	plt.show()
