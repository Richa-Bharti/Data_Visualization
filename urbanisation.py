import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def urbanisation():
	data = pd.read_csv("data/area.csv")

	lables = data['Year']
	urban = data['Urban']
	rural = data['Rural']

	index = np.arange(len(lables))
	width = 0.4

	fig, ax = plt.subplots()
	rects1 = ax.bar(index - width/2, rural, width, label='Rural')
	rects2 = ax.bar(index + width/2, urban, width, label='Urban')

	ax.set_ylabel('Sq. Km')
	ax.set_title('Area - Rural and Urban')
	ax.set_xticks(index)
	ax.set_xticklabels(lables)
	ax.legend()