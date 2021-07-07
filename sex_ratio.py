import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def sex_ratio():
	data = pd.read_csv("data/sex_ratio.csv")

	lables = data['region']
	year2001 = data['2001']
	year2011 = data['2011']

	index = np.arange(len(lables))
	width = 0.4

	fig, ax = plt.subplots()
	rects1 = ax.bar(index - width/2, year2001, width, label='2001')
	rects2 = ax.bar(index + width/2, year2011, width, label='2011')
	
	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(8) 

	ax.set_ylabel('No of females per 1000 males')
	ax.set_title('Sex Ratio of northern states 2001 & 2011')
	ax.set_xticks(index)
	ax.set_xticklabels(lables)
	fig.autofmt_xdate()
	ax.legend()	