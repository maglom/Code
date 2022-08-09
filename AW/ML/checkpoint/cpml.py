# %% [markdown]
# # Checkpoint Machine Learning

# %% [markdown]
# ## Data prep
# 
# 1. Download and import the data, Heart failure: 
# https://www.kaggle.com/andrewmvd/heart-failure-clinical-data 
# Into python. 
# At the link you can see a description of each column, as well as histograms. 

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('ML/checkpoint/heart_failure_clinical_records_dataset.csv')

# %% [markdown]
# 2. We are only going to use the feature columns 
# “DEATH_EVENT, time, age, high_blood_pressure, ejection_fraction, serum_creatinine, 
# serum_sodium”. 
# Extract them from the original dataframe. 

# %%
df = df[['DEATH_EVENT', 'time', 'age', 'high_blood_pressure', 'ejection_fraction', 'serum_creatinine', 'serum_sodium']]

# %% [markdown]
# 3. Create a new column called “age_text”, where the value is “low” for age<=56, “high” for age>= 
# 73 and “medium” for ages between. 
# remove the age column

# %%
df.loc[(df['age'] <= 56), 'age_text'] = 'low'  
df.loc[(df['age'] >= 73), 'age_text'] = 'high'
df.loc[(df['age'] > 56) & (df['age'] < 73), 'age_text'] = 'mid'  

# %% [markdown]
# 4. Use the “from sklearn.preprocessing import OneHotEncoder” and do a one hot encoding of 
# “age_text” and add the three columns to the dataframe with the names “age_text0, age_text1 
# and age_text2”. It is irrelevant which of the columns “low”, “medium” and “high” is placed in 
# which column. Remove the “age_text” from the dataframe. 

# %%
hot_enc = OneHotEncoder()
hot_enc.fit(df[['age_text']])
exp_lvl_columns = hot_enc.transform(df[['age_text']]).toarray()
df1 = pd.DataFrame(exp_lvl_columns, columns=['age_text0', 'age_text1', 'age_text2'])
df = pd.concat([df, df1], axis=1)
df.drop('age_text', axis=1, inplace=True)


# %% [markdown]
#  5. Use one of “from sklearn.preprocessing import MinMaxScaler” or “from sklearn.preprocessing 
# import StandardScaler” and scale the columns “ejection_fraction, serum_creatinine, 
# serum_sodium”. 
# Add the columns back to the dataframe with the column names “ejection_fraction_sc, 
# serum_creatinine_sc, serum_sodium_sc”, and remove the columns “ejection_fraction, 
# serum_creatinine, serum_sodium”. 

# %%
scaler = StandardScaler()
scaler.fit(df[['ejection_fraction', 'serum_creatinine', 'serum_sodium']])
df[['ejection_fraction_sc', 'serum_creatinine_sc', 'serum_sodium_sc']] = scaler.transform(df[['ejection_fraction', 'serum_creatinine', 'serum_sodium']])
df.drop(['ejection_fraction', 'serum_creatinine', 'serum_sodium'], axis=1, inplace=True)

# %% [markdown]
# 6. STRETCH: 
# add more column and do the appropriate scaling for those columns, as well as add log scaling 
# for any column where that seams desirable.  

# %% [markdown]
# ## Classification
# 
# 1. From the prepped dataset above, extract the column “DEATH_EVENT” as y, and “age_text0, 
# age_text1, age_text2, high_blood_pressure, ejection_fraction_sc, serum_creatinine_sc, 
# serum_sodium_sc” as X. 
# use the “np.c_[ ]” to get X and y in numpy format ready for training. 

# %%
y = df['DEATH_EVENT']
X = df[['age_text0', 'age_text1', 'age_text2', 'high_blood_pressure', 'ejection_fraction_sc', 'serum_creatinine_sc', 'serum_sodium_sc']]
y = np.c_[y]
X = np.c_[X]

# %% [markdown]
# 2. Use the “from sklearn.model_selection import train_test_split” and split X and y into X_train, 
# X_test, y_train and y_test. Using a 20% test data size. 

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# %% [markdown]
# 3. Train a logistic regression algorithm on the training data. 

# %%
model = LogisticRegression()
model.fit(X_train, y_train)

# %% [markdown]
# 4. Make prediction using the training and test data, name the prediction variables y_train_pred 
# and y_test_pred.  
# Create a y_test_pred_naive which has the same shape as y_test, but only predicts the most 
# common label. 

# %%
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
y_test_pred_naive = np.zeros((60,1))

# %% [markdown]
# 5. Use “from sklearn.metrics import accuracy_score” and calculate the train, test, and test_naive 
# accuracy. 
# Also using “from sklearn.metrics import confustion_matrix” and print the train, test, and 
# test_naive confusion matrix. 
# What are your conclusion, is the model working well compared to the naive predictions? 

# %%
y_train_acu = accuracy_score(y_train, y_train_pred)
y_test_acu = accuracy_score(y_test, y_test_pred)
y_naive_acu = accuracy_score(y_test, y_test_pred_naive)

print(f'''The model is giving accuracy score of: 
y_train_acu = {y_train_acu}
y_test_acu = {y_test_acu}
The naive prediction:
y_naive_acu = {y_naive_acu}

''')

y_train_conf = confusion_matrix(y_train, y_train_pred)
y_test_conf = confusion_matrix(y_test, y_test_pred)
y_naive_conf = confusion_matrix(y_test, y_test_pred_naive)

print(f'''The model is giving a confusion_matrix score of: 
y_train_acu:
{y_train_conf}
y_test_acu:
{y_test_conf}
The naive prediction:
y_naive_acu:
{y_naive_conf}


I would say this model is not much better than the naive predictions because the score of the naive prediction is 
sometimes better and sometimes just a little lower than the model''')

# %% [markdown]
# 6. STRETCH: 
# Try other models example k-nearest-neighbor, SVM. DecisionTrees, Xgboost, try 
# hyperparameter tuning them. How good an accuracy are you able to get on the test data? 

# %% [markdown]
# ## Regression

# %% [markdown]
# 1. From the prepped dataset above extract all columns, but only the rows where “DEATH_EVENT” 
# is True (or 1). 

# %%
df = df.loc[df['DEATH_EVENT'] == 1]

# %% [markdown]
# 2. From the data with only death instances, extract the column “time” as y, and “age_text0, 
# age_text1, age_text2, high_blood_pressure, ejection_fraction_sc, serum_creatinine_sc, 
# serum_sodium_sc” as X. 
# use the “np.c_[ ]” to get X and y in numpy format ready for training. 

# %%
y = np.c_[df['time']]
X = np.c_[df[['age_text0', 'age_text1', 'age_text2', 'high_blood_pressure', 'ejection_fraction_sc', 'serum_creatinine_sc', 'serum_sodium_sc']]]

# %% [markdown]
# 3. Use the “from sklearn.model_selection import train_test_split” and split X and y into X_train_r, 
# X_test_r, y_train_r and y_test_r. Using a 20% test data size. 

# %%
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y, test_size=0.2)

# %% [markdown]
# 4. Train a linear regression algorithm on the training data. 

# %%
model_reg = LinearRegression()
model_reg.fit(X_train_r, y_train_r)

# %% [markdown]
# 5. Make prediction using the training and test data, name the prediction variables y_train_pred_r 
# and y_test_pred_r.  
# Create a y_test_pred_naive_r which has the same shape as y_test_r, but only predicts the 
# average time for the patients who died. 

# %%
y_train_pred_r = model_reg.predict(X_train_r)
y_test_pred_r = model_reg.predict(X_test_r)
mean_train = np.mean(y_train_r) #litt usikker på om det blir riktig med snitt av hele datasettet men landet på at det er bedre å ta utgangspunkt i train-datasettet.
y_test_pred_naive_r = np.full((20, 1), mean_train)

# %% [markdown]
# 7. Use “from sklearn.metrics import mean_square_error” and “from sklearn.metrics import 
# mean_absolute_error” and calculate the train, test, and test_naive scores.  
# What are your conclusion, is the model working well compared to the naive predictions? 

# %%
mse_train = mean_squared_error(y_train_r, y_train_pred_r)
mse_test = mean_squared_error(y_test_r, y_test_pred_r)
mse_naive = mean_squared_error(y_test_r, y_test_pred_naive_r)

mae_train = mean_absolute_error(y_train_r, y_train_pred_r)
mae_test = mean_absolute_error(y_test_r, y_test_pred_r)
mae_naive = mean_absolute_error(y_test_r, y_test_pred_naive_r)

print(f'''
mse_train = {mse_train}
mse_test =  {mse_test}
mse_naive = {mse_naive}

mae_train = {mae_train}
mae_test =  {mae_test}
mae_naive = {mae_naive}

I would say the model is not much better than the naive predictions. 
The model does not consistently outperform the naive prediction, and when it does outperform it is not by a large value.
''')

# %% [markdown]
# 8. STRECH: 
# Try other models example k-nearest-neighbor, SVM. DecisionTrees, Xgboost, try 
# hyperparameter tuning them. How good an MSE and MAE are you able to get on the test data? 


