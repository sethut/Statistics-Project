###매매가 변동 크기###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def run(arg_month):	
	rc('font', family='AppleGothic')
	meme = pd.read_csv("meme_change.csv", encoding="utf-8")
	date=list(meme)
	date_list=date[1:]
	region=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']
	region2=['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충청도','전라도','경상도']
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
	    rslt.append(arg_month*reg.coef_[0][0] + reg.intercept_[0])

	count=0
	
	map_region_list=[]
	map_pd = pd.read_csv("data_draw_korea.csv", encoding="utf-8")
	for i in range(len(region2)) :
    		map_region_list.append([dec for dec in map_pd['광역시도'] if region2[i] in dec])
	for i in range(len(map_region_list)):
		for j in range(len(region2)):
			if map_region_list[i][0] == region2[j]:
				map_pd.loc[count:count+len(map_region_list[i]),['땅 값']] = rslt[j]
				count+=len(map_region_list[i])
	print(map_pd)
	map_pd.head()
	BORDER_LINES = [
	    [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천
	    [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울
	    [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
	     (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도
	    [(9, 12), (9, 10), (8, 10)], # 강원도
	    [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
	     (13, 4), (14, 4), (14, 2)], # 충청남도
	    [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
	     (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도
	    [(14, 4), (15, 4), (15, 6)], # 대전시
	    [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)], # 경상북도
	    [(14, 8), (16, 8), (16, 10), (15, 10),
	     (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시
	    [(15, 11), (16, 11), (16, 13)], # 울산시
	    [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도
	    [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시
	    [(18, 5), (20, 5), (20, 6)], # 전라남도
	    [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시
	]

	gamma = 0.75

	blockedMap = map_pd
	targetData = '땅 값'

	whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData])) * 0.25 + min(blockedMap[targetData])

	datalabel = targetData

	vmin = min(blockedMap[targetData])
	vmax = max(blockedMap[targetData])
	
	mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
	masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
	cmapname = 'Blues' #'Reds'

	plt.figure(figsize=(7, 8))
	plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)

	# 지역 이름 표시
	for idx, row in blockedMap.iterrows():
	    annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
	    
	    # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다. (중구, 서구)
	    if row['광역시도'].endswith('시') and not row['광역시도'].startswith('세종'):
	        dispname = '{}\n{}'.format(row['광역시도'][:2], row['행정구역'][:-1])
	        if len(row['행정구역']) <= 2:
	            dispname += row['행정구역'][-1]
	    else:
	        dispname = row['행정구역'][:-1]
	
	    # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
	    if len(dispname.splitlines()[-1]) >= 3:
	        fontsize, linespacing = 9.5, 1.5
	    else:
	        fontsize, linespacing = 11, 1.2
	
	    plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
	                 fontsize=fontsize, ha='center', va='center', color=annocolor,
	                 linespacing=linespacing)
    
	# 시도 경계 그린다.
	for path in BORDER_LINES:
	    ys, xs = zip(*path)
	    plt.plot(xs, ys, c='black', lw=4)

	plt.gca().invert_yaxis()
	#plt.gca().set_aspect(1)

	plt.axis('off')
    
	cb = plt.colorbar(shrink=.1, aspect=10)
	cb.set_label(datalabel)

	plt.tight_layout()
	plt.show()
	#date_list=date[1:]
	# region=['서울-강북지역','서울-강남지역','경기','인천',
    #     '부산','대구','광주','대전','울산','세종','강원',
    #     '충청도','전라도','경상도']
    
    
    #current_increase=[178186.75, 195022 ,40445.5,33227,49081,123129,102768,59371,34547,172333,34972,17984.5,14926,35582]
	#ratio_col=set(ratio.iloc[1].values)
	# meme_list=meme['지 역'].values
	# meme_money=[]
	# for i in range(0,len(meme_list)):
	# 	meme_money.append(meme.iloc[i].values[1:])
	   

	# year_list=list(meme)
	

	# a=[]
	# rslt=[]
	# for i in range(1,len(year_list)):
	#     a.append(i)

	# ### DataFrame 생성 ###
	# meme_df = pd.DataFrame(index = date_list) 
	# for i in range(0,len(meme_list)):
	# 	meme_df[meme_list[i]]=meme.loc[i]
	
	# meme_df['month']=a
	# for i in range(len(region)):
	#     x = meme_df.loc[:,["month"]]
	#     y = meme_df.loc[:,[region[i]]]
	#     from sklearn import linear_model
	#     reg = linear_model.LinearRegression()
	#     reg.fit(x,y)
	#     print( "R²=", reg.score(x,y) )
	#     print( "coefficient=", reg.coef_ )
	#     print( "intercept=", reg.intercept_ )
	#     print( region[i] , " : ", arg_month*reg.coef_[0][0] + reg.intercept_[0])
	#     rslt.append(arg_month*reg.coef_[0][0] + reg.intercept_[0])


	# ### MatePlot 생성 ### 
	# plt.figure(figsize=(7,7))
	# plt.bar(region,rslt)
	# plt.rcParams['axes.unicode_minus'] = False

	# plt.show()
#run(92)
