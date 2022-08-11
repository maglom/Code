import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
%matplotlib inline
import sklearn.preprocessing as pre

df = pd.read_csv('kc_house_data.csv')

df.drop(['id', 'date'], axis=1, inplace=True)

x_columns = ['sqft_living', 'bathrooms', 'bedrooms']

y_columns = ['price']

X_train, X_test, y_train, y_test = train_test_split(
    df, df)

X_train = np.c_[X_train[x_columns]]
y_train = np.c_[y_train[y_columns]]
X_test = np.c_[X_test[x_columns]]
y_test = np.c_[y_test[y_columns]]

model = KNeighborsRegressor(50)
model.fit(X=X_train, y=y_train)

y_pred = model.predict(X_test)

score = model.score(X=X_test, y=y_test)

mae = mean_absolute_error(y_test, y_pred)

mse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f'''Score before prep
Score: {score}
mae: {mae}
mse: {mse}
''')

minmax = pre.MinMaxScaler()

minmax.fit(df[x_columns])

df[x_columns] = minmax.transform(df[x_columns])

X_train, X_test, y_train, y_test = train_test_split(
    df, df)

X_train = np.c_[X_train[x_columns]]
y_train = np.c_[y_train[y_columns]]
X_test = np.c_[X_test[x_columns]]
y_test = np.c_[y_test[y_columns]]

model = KNeighborsRegressor(50)
model.fit(X=X_train, y=y_train)

y_pred = model.predict(X_test)

score = model.score(X=X_test, y=y_test)

mae = mean_absolute_error(y_test, y_pred)

mse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f'''Score after prep
Score: {score}
mae: {mae}
mse: {mse}
''')