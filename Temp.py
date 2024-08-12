
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge


from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import r2_score, mean_squared_error





################################################################ Pandas
#######################################################################
data = {'Name': ['Tom', 'Nick', 'Anna', 'Mo', 'Jon', 'Mike', 'Arec',  'Ali'],
        'Zipcode' : [193420, 234518, 412354, 992354, 412354, 124104, 112354, 488854],
        'Married': [0, 0, 1, 1, 1, 0, 0, 1],
        'Kid': [0, 0, 1, 1, 1, 0, 1, 0],
        'Age': [19, 21, 35, 71, 65, 12, 25, 21],
        'Salary': [100, 120, 110, 200, 180, 50, 130, 112]}

df = pd.DataFrame(data)

X = df.drop(columns=["Salary"])
y = df[["Kid"]]


# Split the test-train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y)


# -------------------- Feature Scaling
# -----------------------------------
#If SGD: Scale features to have mean 0, variance 1. Returns numpy array
scaler = StandardScaler()
cols = ['Married', 'Age']

X_train = scaler.fit_transform(X_train[cols])
X_test = scaler.transform(X_test[cols])



# Define which model you want to use
model = RandomForestClassifier()
# model = LinearRegression() # compute using direct matrix multiplication
# regressor = SGDRegressor(max_iter=1000,  # Number of epochs
#                          eta0=0.01,      #  Initial learning rate
#                          learning_rate='constant')  # How the learning rate changes over time (across epochs). Options: 'constant', 'optimal', 'invscaling', 'adaptive'



# Train the model
model.fit(X_train, y_train)

# ------------------------------------
# Predict on test data
y_pred = model.predict(X_test)

print("y_pred ", y_pred)
print("y_test ", y_test)


# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

TN, FP, FN, TP = confusion_matrix(y_test, y_pred).ravel()
print(TN, FP, FN, TP)