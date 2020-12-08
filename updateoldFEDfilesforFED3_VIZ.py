
import pandas as pd
import os
from pandas import read_csv

'INPUT'
# enter path to FED file
filename = '/path/to/FED011_071219_00.CSV'

path = os.path.dirname (filename)

df = pd.read_csv(filename)
#print (df)

# combining day and hour column to one time column
df["MM:DD:YYYY hh:mm:ss"] = df.iloc[:, 0].map(str) + ' ' + df.iloc[:, 1].map(str)

# delete old day and hour columns
df.drop(df.iloc[:, 0:2], inplace = True, axis = 1) 

# move time column to front
col = df.pop("MM:DD:YYYY hh:mm:ss")
df.insert(0, col.name, col)

# adding new column "Event" as 6th column
df.insert(5, "Event", '', True) 

# rename column FR_Ratio to "Session_Type"
df.rename(columns = {' FR_Ratio':'Session_Type'}, inplace = True)

#print (df)


'OUTPUT'
# Save updated FEDfile in same directory as filename_new
df.to_csv(os.path.join(path,os.path.basename (filename) + "_new" + ".csv"), index = False)

print("Printed new CSV")