"""import pandas as pd
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
    # "db_Nov13_v4.csv", na_values=['NA', '?'])
    "trainingData.csv", na_values=['NA', '?'])

# Convert to numpy classificatin
x = df[['questionID', 'tsStamp', 'pulse', 'skin_conductivity', 'respiration_belt',
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

# file = open(filename, "r")


#example_Array = [7, 0, 24.355373, 0, 0, 15.9444809], [3, 1, 24.355373, 0, 0, 15.9444809], [4, 174.9313343, 0, 0,
#                                                                                       11.31177802, 0]
# another_array = np.fromfile()

my_data = np.genfromtxt('dataSetFile.csv', delimiter=',', dtype=float)
accData = np.resize(my_data, (len(my_data) - 1, 6))
finData = np.resize(accData, (9, 6))
print(finData[0])
curQID = accData[0][0]
tsStamp = 0.0
pulse = 0.0
skin_conductivity = 0.0
respiration_belt = 0.0
blood_pressure = 0.0
counter = 0.1
for x in accData:
    if curQID != x[0]:
        curQID = x[0]
        tsStamp += x[1]
        pulse += x[2]
        skin_conductivity += x[3]
        respiration_belt += x[4]
        blood_pressure += x[5]
        counter += 1
    else:
        np.insert(finData, 1, (curQID, tsStamp/counter, pulse/counter, skin_conductivity/counter, respiration_belt/counter, blood_pressure/counter))
        curQID = x[0]
        tsStamp = x[1]
        pulse = x[2]
        skin_conductivity = x[3]
        respiration_belt = x[4]
        blood_pressure = x[5]
        counter = 0.1

print(finData)


sample_flower = np.array(finData, dtype=float)
pred = model.predict(sample_flower)
#print(pred)
pred = np.argmax(pred, axis=1)
file = open("mlResult.txt", "w")
count = 0
for x in sample_flower:
    file.write(f"Predict that {sample_flower[count]}  Question: {count+1} is {species[pred][count]} \n")
    print(f"Predict that {sample_flower[count]} Question: {count+1} is {species[pred][count]}\n")
    count += 1
file.close()"""
