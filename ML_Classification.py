"""""''''# import mysql
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
    "db_Nov13_v4.csv", na_values=['NA', '?'])

# Convert to numpy classificatin
x = df[['questionID', 'response', 'tsStamp', 'pulse', 'skin_conductivity', 'respiration_belt',
        'blood_pressure']].values
dummies = pd.get_dummies(df['actual_ans'])  # Classification (labelling)
species = dummies.columns
y = dummies.values

# Build Neural network
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation='relu'))  # Hidden 1
model.add(Dense(25, activation='relu'))  # Hidden 2
model.add(Dense(y.shape[1], activation='softmax'))  # Output
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x, y, verbose=2, epochs=100)

print(species)

pred = model.predict(x)
# print(f"Shape: {pred.shape}")
np.set_printoptions(suppress=True)
predict_classes = np.argmax(pred, axis=1)
expected_classes = np.argmax(y, axis=1)
# print(f"Predictions: {predict_classes}")
# print(f"Expected: {expected_classes}")

print(species[predict_classes[1:10]])

correct = accuracy_score(expected_classes, predict_classes)
print(f"Accuracy: {correct}")

filename = "datafile.txt"
# file = open(filename, "r")
maxpred = ""

counter = 0
rigthSample = ""
with open(filename) as file:
    for line in file:
        # print(line.rstrip())
        splitLine = line.split(',')
        singleEntry = splitLine[0:len(splitLine) - 1]
        sample_flower = np.array(singleEntry, dtype=float)
        pred = model.predict(sample_flower)
        if counter == 0:
            maxpred = pred
            counter = 1
            rigthSample = sample_flower
        elif(np.argmax(pred) > np.argmax(maxpred)):
            maxpred = pred
            rigthSample = sample_flower

    #print(dataset)

pred = model.predict(rigthSample)
print(maxpred)  # False , True
pred = np.argmax(maxpred, axis=1)
print(f"Predict that {rigthSample} is: {species[maxpred]}")
os.system(f"echo  {species[maxpred]} with a accuracy of {maxpred} > prediction.txt")"""""