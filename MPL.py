import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(pennData)

print(df.describe())
print(df.info())

df.groupby('Year')['GPA'].mean()
plt.show()