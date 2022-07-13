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

try:
    df = pd.read_csv('kc_house_data.csv')
    
except:
    df = pd.read_csv('AW/ML/kc_house_data.csv')

df_test, df_train = train_test_split(df, test_size=0.3)

input = df[['sqft_living', 'grade']]

x_multi_colum = np.c_[input]

price = np.c_[df['price']]

model = KNeighborsRegressor(2)

model.fit(X=x_multi_colum, y=price)

model.score(X=x_multi_colum, y=price)

price_pred = model.predict(np.c_[input])

mean_absolute_error(price_pred, price)



