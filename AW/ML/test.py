import matplotlib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


try:
    df = pd.read_csv('kc_house_data.csv')
    
except:
    df = pd.read_csv('AW/ML/kc_house_data.csv')

df.drop(['date'], axis=1)

plt.hist