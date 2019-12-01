import pandas as pd
import matplotlib.pyplot as plt
import m

def run(arg_yesan,arg_month,arg_region,building_check):
	pd_csv = pd.read_csv('meme.csv')
	year_list=list(pd_csv)
	a=[]
	for i in range(1,len(year_list)):
	    a.append(i)
	region=['선 택','서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']
	
	df = pd.DataFrame({
	    'month' : a,
	    'meme' : pd_csv.loc[region.index(arg_region)-1][1:]
	})
	X = df.loc[:,['month']]
	y = df.loc[:,['meme']]
	new_x=[]
	for i in range(1,52):
	    new_x.append(i)

	from sklearn import linear_model
	reg = linear_model.LinearRegression()
	reg.fit(X,y)
	print("x=",X)
	print("y=",y)
	print( "R²=", reg.score(X,y) )
	print( "coefficient=", reg.coef_ )
	print( "intercept=", reg.intercept_ )
	new_y=[]
	for i in range(0,len(new_x)):
	    new_y.append(reg.coef_ * new_x[i] + reg.intercept_)
	    
	new_y2=[]
	for i in range (0,len(new_y)):
	    new_y2.append(new_y[i][0])

	    ###deep learning result###
	deep_x=[]
	deep_y=[]
	for i in range(0,arg_month):
	    deep_x.append(i)

	for i in range(0,arg_month):
	    deep_y.append(reg.coef_ * deep_x[i] + reg.intercept_)
	
#	### MatePlot 생성 ### 
#	plt.figure(figsize=(7,7))
#	plt.plot(deep_x,deep_y,label=arg_region)
#	plt.legend(region_list,loc = 'upper left',ncol=4,bbox_to_anchor=(1, 1)) 
#	rc('font', family='AppleGothic')
#	plt.rcParams['axes.unicode_minus'] = False
#	plt.show()
	if building_check==0:
			m.run(arg_yesan,arg_month,arg_region,reg.coef_[0][0]*arg_month + reg.intercept_[0],building_check)
	else:
    		m.run(arg_yesan,arg_month,arg_region,reg.coef_[0][0]*arg_month + reg.intercept_[0],4000*50*4)
#print(reg.coef_[0][0]*arg_month + reg.intercept_[0])
