import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model



def main():

	df= pd.read_csv(r'C:\Users\Aarti Ingle\Desktop\Python\predict\src\day.csv',index_col = 0)

	#print(df.head())
	#print(df.describe())
	#print(df.dtypes)
	
	df.dteday=pd.to_datetime(df.dteday)
	#print(df.isna().sum())
	#print(df.corr())
	return df
	
	
def plot():
	
	plt.style.use('seaborn')
	
	df=main()
	print(df.head())
	print(df.describe())
	
	fig= plt.figure()
	ax=fig.add_subplot(221)
	
	ax.scatter(df.atemp[df.dteday<'2011-12-31'], df.cnt[df.dteday<'2011-12-31'], c='r', label= 'atemp',alpha=0.6,linewidth=1,edgecolor='black')
	plt.legend()
	#ax.set_xlabel('atemp')
	ax.set_ylabel('cnt')
	
	ax=fig.add_subplot(222)
	ax.scatter(df.hum[df.dteday<'2011-12-31'],df.cnt[df.dteday<'2011-12-31'],c='b', label='hum',alpha=0.5,linewidth=1,edgecolor='black')
	plt.legend(loc='upper left')
	ax.set_ylabel('cnt')
	
	ax=fig.add_subplot(223)
	ax.scatter(df.windspeed[df.dteday<'2011-12-31'],df.cnt[df.dteday<'2011-12-31'],c='g', label='windspeed', alpha=0.5,linewidth=1,edgecolor='black')
	plt.legend()
	ax.set_ylabel('cnt')
	#ax = fig.add_subplot(224)
	
	plt.show()

if __name__=="__main__":
	plot()

def input_values():
 
	p_atemp = float(input("Enter the atemp(normalize temperature) value between 0.840896 and 0.079070 : "))
	if (p_atemp > 0.840896 or p_atemp < 0.079070):
		raise ValueError('atemp should be the value between 0.840896 and 0.079070')
			
		
	p_hum= float(input("Enter the hum(humadity) value between 0.972500 and 0.000: "))
	if (p_hum>0.972500 or p_hum<0.000000):
		raise ValueError('humadity should be the value between 0.972500 and 0.000')
			
			
	p_windspeed= float(input("Enter the windspeed value between 0.507463 and 0.022392 : "))
	if (p_windspeed>0.507463 or p_windspeed<0.022392):
		raise ValueError('windspeed should be the value between 0.507463 and 0.022392')
	
		
	return p_atemp,p_hum,p_windspeed
	
	
	
def predict_cnt(p_atemp,p_hum,p_windspeed):

	
	if (p_atemp > 0.840896 or p_atemp < 0.079070):
		raise ValueError('atemp should be the value between 0.840896 and 0.079070')
	if (p_hum>0.972500 or p_hum<0.000000):
		raise ValueError('humadity should be the value between 0.972500 and 0.000')
	if (p_windspeed>0.507463 or p_windspeed<0.022392):
		raise ValueError('windspeed should be the value between 0.507463 and 0.022392')
	
	i,j,k = p_atemp,p_hum,p_windspeed
	
	df=main()
	
	atemp=df.atemp[df.dteday<'2011-12-31']
	hum=df.hum[df.dteday<'2011-12-31']
	windspeed=df.windspeed[df.dteday<'2011-12-31']
	dataset_train=pd.concat([atemp,hum,windspeed], axis=1)
	label_train = df.cnt[df.dteday<'2011-12-31']
	
	#print(type(dataset_train))
	#print('dataset length:',len(dataset_train),'label length:',len(label_train))
	
	model = linear_model.LinearRegression()
	model.fit(dataset_train,label_train)
	#regressionline(model,dataset_train,label_train,"count for casual")
	
	
	#we can also create the seperate dataset and label set for testing the model and then test the score(R2) for this sets.
	tatemp=df.atemp[df.dteday>'2011-12-31']
	thum=df.hum[df.dteday>'2011-12-31']
	twindspeed=df.windspeed[df.dteday>'2011-12-31']
	dataset_test=pd.concat([tatemp,thum,twindspeed], axis=1)
	label_test = df.cnt[df.dteday>'2011-12-31']
	
	
	test_casual= i,j,k
	test_casual=list(test_casual)
	
	predict_count= model.predict([test_casual])
	R2=model.score(dataset_train,label_train)
	predict_count=int(predict_count)
	R2 = R2*100
	
	#print("Total count, R2: ",predict_count,',',R2)
	
	
	
	return predict_count
	
