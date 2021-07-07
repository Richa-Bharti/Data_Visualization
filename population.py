import matplotlib.pyplot as plt
import pandas as pd


def population():
	data = pd.read_csv("data/population.csv")
	plt.plot(data["Year"], data["Population"]/10000000)
	plt.title('Population of Delhi (1955 to 2019)')
	plt.xlabel('Year')
	plt.ylabel('Population\n(crore)')