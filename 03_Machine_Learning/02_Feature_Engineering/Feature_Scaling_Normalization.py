import matplotlib.pyplot as plt
import pandas as pd  # data processing
import seaborn as sns

df = pd.read_csv(
    "https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/refs/heads/main/day25-normalization/wine_data.csv",
    header=None,
    usecols=[0, 1, 2]
)

df.columns = ['Class label', 'Alcohol', 'Malic acid']

print(df.head())

plt.plot(df['Alcohol'])
plt.title("Alcohol Feature")
plt.xlabel("Index")
plt.ylabel("Alcohol")
plt.show()
sns.kdeplot(df['Malic acid'])# type: ignore
