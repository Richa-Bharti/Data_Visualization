import matplotlib.pyplot as plt
import pandas as pd



def age():
	data = pd.read_csv("data/age.csv")

	lables = data['age']
	title = [1991, 2001, 2011]
	plt.suptitle('Distribution of ages')
	for num in range(3):
		years = data[str(title[num])]/100000
		plt.subplot(1,3,num+1)
		plt.bar(lables, years)
		plt.tick_params(gridOn=True)
		plt.tick_params(grid_alpha = 190)
		plt.tick_params(labelsize=6)
		plt.tick_params(labelrotation=45)

		plt.title(title[num])