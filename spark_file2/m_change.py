###매매가 변동 크기###
import pandas as pd
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def run():
	meme = pd.read_csv("meme.csv", encoding="utf-8")
	date=list(meme)
	date_list=date[1:]

	#ratio_col=set(ratio.iloc[1].values)
	meme_list=meme['지 역'].values
	meme_list
	meme_money=[]
	for i in range(0,len(meme_list)):
		meme_money.append(meme.iloc[i].values[1:])
    
    
	### DataFrame 생성 ###
	meme_df = pd.DataFrame(columns = ['지 역','날 짜','가 격'])

	for i in range(0,len(meme_list)):
		meme_diff=np.diff(meme_money[i])
		meme_diff_list=meme_diff.tolist()
		meme_df.loc[i] = [meme_list[i], date_list[meme_diff_list.index(max(meme_diff))],max(meme_diff)]

	meme_df_sort=pd.DataFrame(meme_df.sort_values(by=['가 격'],ascending=False))
	meme_df=meme_df_sort.reset_index(drop=True)
	meme_df
