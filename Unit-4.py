
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print(df.head())

df.info()

print("Average:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())


print("Students scoring above 75:")
print(df[df["Marks"] > 75])


df.plot(x="Student_Name", y="Marks", kind="bar")
plt.show()


df["Marks"].plot(kind="hist")
plt.show()

plt.scatter(df["Roll_Number"], df["Marks"])
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.show()
