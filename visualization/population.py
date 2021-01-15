import pandas as pd
from matplotlib import pyplot as plt

def population():
    
    state_data= pd.read_csv("data/state.csv")
    DL = state_data[state_data.state =='Delhi']
    MB = state_data[state_data.state=='Mumbai']
    plt.plot(DL.year,DL.population/10000000)
    plt.plot(MB.year,MB.population/10000000)
    plt.title("Population Growth: Mumbai v/S Delhi")
    plt.xlabel("year")
    plt.ylabel("population growth")
    plt.legend(["Delhi ","Mumbai"])
