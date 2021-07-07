import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import urbanisation
import sex_ratio
import population
import age


def show_menu():
	print()
	print("1. Rapid Urbanisation")
	print("2. Population")
	print("3. Sex Ratio")
	print("4. Age distribution")
	print("5. Exit")
	print()

def show_graph():
	plt.tick_params(gridOn=True)
	plt.tick_params(grid_alpha = 190)
	plt.show()


print("Welcome to our project.")
print("A visualisation of Demographics of Delhi.")

while True:
	show_menu()
	choice = int(input("Enter your choice: "))

	if choice == 1:
		urbanisation.urbanisation()
	elif choice == 2:
		population.population()
	elif choice == 3:
		sex_ratio.sex_ratio()
	elif choice == 4:
		age.age()
	elif choice == 5:
		break
	else:
		print("Invalid choice.\n")

	show_graph()