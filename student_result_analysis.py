import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {
    "Name": ["Ramya", "Anil", "Sita", "Ravi", "Kiran"],
    "Gender": ["Female", "Male", "Female", "Male", "Male"],
    "Result": ["Pass", "Fail", "Pass", "Fail", "Pass"]
}
df = pd.DataFrame(data)
le = LabelEncoder()
df["Gender_Encoded"] = le.fit_transform(df["Gender"])
df["Result_Encoded"] = le.fit_transform(df["Result"])
print(df)
