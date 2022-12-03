import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as numpy
from joblib import dump, load

bike_data = pd.read_csv('daily_bike.csv')
X = bike_data[['season','mnth','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed']].values
y = bike_data['rentals'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

model = LinearRegression().fit(X_train, y_train)
predicitions = model.predict(X_test)

print(X_test[0])
print(predicitions[0])

dump(model, 'model.joblib')

model_load = load('model.joblib')
predicitions = model_load.predict(X_test)
print(predicitions[:2])