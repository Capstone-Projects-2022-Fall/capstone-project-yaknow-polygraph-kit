import mysql
import pandas as pd
import SingularRecordingsDB
import io
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import accuracy_score

#TODO, ask Thomos to install mysql-shell package on the server or ask for permission to do it your self
'''db_con = mysql.connector.connect(
    host="173.255.232.150",
    user="cis4398",
    passwd="dNC=IK~9)7",
    database="Questions"
)
df = pd.read_sql("SELECT exmaID, questionID, question, response, tsStamp, pulse, skin_conductivity, respiration_belt, blood_pressure, actual_ans  FROM SingularRecording;", db_con)
db_con.close()'''

df = pd.read_csv(
    "",
    na_values=['NA', '?'])


#Convert to numpy classificatin
x = df[['exmaID', 'questionID', 'question', 'response', 'tsStamp', 'pulse', 'skin_conductivity', 'respiration_belt', 'blood_pressure']].values
dummies = pd.get_dummies(df['actual_ans']) # Classification (labelling)
species = dummies.columns
y = dummies.values






