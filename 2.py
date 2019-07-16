
import pickle
import re
import pandas as pd
import parselmouth
import csv

sound = parselmouth.Sound("Phonation_2.wav")
pitch = sound.to_pitch()
pulses = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")
voice_report_str = parselmouth.praat.call([sound, pitch, pulses], "Voice report", 0.0, 0.0, 75, 600, 1.3, 1.6, 0.03, 0.45)
 
s=re.findall(r'-?\d+\.?\d*',voice_report_str)
df = pd.DataFrame(s)
df.to_csv("file_path.csv")
row = ['1',s[21], s[22]+'E'+s[23],s[24],s[26],s[27],s[28],s[29],s[31],s[33],s[35],s[36],s[37],s[38],s[39],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10]+'E'+s[11],s[12]+'E'+s[13]]

with open('test.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines[1] = row

with open('test.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()

svm_pkl_filename = 'svmclassifier.pkl'

decision_tree_model_pkl = open(svm_pkl_filename, 'rb')
svm_model = pickle.load(decision_tree_model_pkl)

data = pd.read_csv('test.csv')
X_test1=data.iloc[:,[5,23,22,13,1,7,2,4,12,3]].values
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X_test1=sc.transform(X_test1)

y_pred = svm_model.predict(X_test1)

#print(y_pred)

