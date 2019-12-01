# from keras.models import Sequential
# from keras.layers import Dense
# from sklearn.model_selection import train_test_split

# import pandas as pd

# df = pd.read_csv('house_price.csv', delim_whitespace=True, header=None)

# data_set = df.values
# X = data_set[:, 0:13]
# Y = data_set[:, 13]

# # X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y,
# #                                                                 test_size=0.2)

# # model = Sequential()
# # model.add(Dense(30, input_dim=13, activation='relu'))
# # model.add(Dense(6, activation='relu'))
# # model.add(Dense(1))

# # model.compile(loss='mean_squared_error', optimizer='adam')

# # model.fit(X_train, Y_train, epochs=200, batch_size=10)

# # Y_prediction = model.predict(X_validation).flatten()

# # for i in range(10):
# #   real_price = Y_validation[i]
# #   predicted_price = Y_prediction[i]
# #   print('Real Price: {:.3f}, Predicted Price: {:.3f}'.format(real_price,
# #                                                              predicted_price))

import pandas as pd
import matplotlib.pyplot as plt

pd_csv = pd.read_csv('meme.csv')
year_list=list(pd_csv)
a=[]
for i in range(1,len(year_list)):
    a.append(i)

df = pd.DataFrame({
    'month' : a,
    'meme' : pd_csv.loc[2][1:]
# #'height': [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83],
# #'mass': [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46],
})

print(df)


#han_x=[1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
#han_y=[52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]
#han_x=[1,2]
#han_y=pd_csv.iloc[2]

# #print(han_y)

X = df.loc[:,['month']]
y = df.loc[:,['meme']]

new_x=[]
for i in range(1,52):
    new_x.append(i)

#print(pd_csv.loc[2])



from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X,y)
print( "R²=", reg.score(X,y) )
print( "coefficient=", reg.coef_ )
print( "intercept=", reg.intercept_ )


new_y=[]
for i in range(0,len(new_x)):
    new_y.append(reg.coef_ * new_x[i] + reg.intercept_)
print(new_x)
new_y2=[]
for i in range (0,len(new_y)):
    new_y2.append(new_y[i][0])

	
result=[]
plt.plot(X,y)
plt.plot(new_x,new_y2)
plt.show()

User_X=int(input())
print(reg.coef_[0][0]*User_X + reg.intercept_[0])

