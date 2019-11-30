import pandas as pd
import matplotlib.pyplot as plt

def run(arg_month,arg_region):
	pd_csv = pd.read_csv('meme.csv')
	year_list=list(pd_csv)
	a=[]
	for i in range(1,len(year_list)):
	    a.append(i)

	region=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충북','충남','전북','전남','경북','경남','제주']
	print(region[region.index(arg_region)])
	df = pd.DataFrame({
	    'month' : a,
	    'meme' : pd_csv.loc[region.index(arg_region)][1:]
	})
	X = df.loc[:,['month']]
	y = df.loc[:,['meme']]
	
	new_x=[]
	for i in range(1,52):
	    new_x.append(i)

	from sklearn import linear_model
	reg = linear_model.LinearRegression()
	reg.fit(X,y)
	print( "R²=", reg.score(X,y) )
	print( "coefficient=", reg.coef_ )
	print( "intercept=", reg.intercept_ )


	new_y=[]
	for i in range(0,len(new_x)):
	    new_y.append(reg.coef_ * new_x[i] + reg.intercept_)
	new_y2=[]
	for i in range (0,len(new_y)):
	    new_y2.append(new_y[i][0])
	print(reg.coef_[0][0]*arg_month + reg.intercept_[0])

