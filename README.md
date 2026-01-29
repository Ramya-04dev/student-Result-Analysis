import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {
    "Name": ["Ramya", "Anil", "Sita", "Ravi", "Kiran"],
    "Gender": ["Female", "Male", "Female", "Male", "Male"],
    "Marks": [78, 45, 88, 32, 66]
}
df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
le = LabelEncoder()
df["Gender_Encoded"] = le.fit_transform(df["Gender"])
df["Result_Encoded"] = le.fit_transform(df["Result"])
total_students = len(df)
passed_students = (df["Result"] == "Pass").sum()
failed_students = (df["Result"] == "Fail").sum()
print("----- Student Result Analysis -----")
print(df)
print("\nTotal Students:", total_students)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
