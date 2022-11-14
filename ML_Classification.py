# import mysql
import pandas as pd
# import SingularRecordingsDB - UNCOMMENT WHEN USING DB IN SERVER, MUST ADD ADD THE FILE TO SERVER AS WELL
import io
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import accuracy_score
import os

# TODO, ask Thomos to install mysql-shell package on the server or ask for permission to do it your self
'''db_con = mysql.connector.connect(
    host="173.255.232.150",
    user="cis4398",
    passwd="dNC=IK~9)7",
    database="Questions"
)
df = pd.read_sql("SELECT exmaID, questionID, question, response, tsStamp, pulse, skin_conductivity, respiration_belt, blood_pressure, actual_ans  FROM SingularRecording;", db_con)
db_con.close()'''

df = pd.read_csv(
    "db_Nov13_v3.csv", na_values=['NA', '?'])

# Convert to numpy classificatin
x = df[['response', 'tsStamp', 'pulse', 'skin_conductivity', 'respiration_belt',
        'blood_pressure']].values
dummies = pd.get_dummies(df['actual_ans'])  # Classification (labelling)
species = dummies.columns
y = dummies.values

#Build Neural network
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation='relu')) # Hidden 1
model.add(Dense(25, activation='relu')) # Hidden 2
model.add(Dense(y.shape[1],activation='softmax')) # Output

model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(x,y,verbose=2,epochs=100)

print(species)
