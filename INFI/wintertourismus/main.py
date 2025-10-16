import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# 1.3
df: pd.DataFrame = pd.read_excel("./Zeitreihe-Winter-2024011810.xlsx", skiprows=2)
df = df.iloc[1:].reset_index(drop=True)
df.columns = ["x" + str(col) if isinstance(col, int) else col for col in df.columns]

print(df.head())

# 2.1
innsbruck_row = df.loc[df["Gemeinde"].str.strip() == "Innsbruck"].values[0, 3:]
x_years = [int(col[1:]) for col in df.columns[3:]]


plt.figure(figsize=(12, 6))

plt.scatter(
    x_years,
    innsbruck_row,
    color="red",
    marker="o",
    s=50,
    label="Nächtigungen in Innsbruck",
)

plt.plot(x_years, innsbruck_row, linestyle="-", color="gray", alpha=0.5)

plt.title("Zeitlicher Verlauf der Nächtigungen in Innsbruck (Wintersaison)")
plt.xlabel("Wintersaison (Jahr)")
plt.ylabel("Anzahl der Nächtigungen")

plt.xticks(x_years[::2], rotation=45)

plt.grid(True, linestyle="--", alpha=0.6)

plt.legend()
plt.tight_layout()
plt.savefig("data/innsbruck_plot.png")

# 2.2
bezirk_df = df[df["Bez"].str.strip() == "IL"]
bezirk_sum = bezirk_df.iloc[:, 3:].sum(axis=0)

plt.figure(figsize=(12, 6))
plt.plot(x_years, bezirk_sum, marker="o", linestyle="-")
plt.title("Wachstum des Bezirks Innsbruck-Land")
plt.xlabel("Wintersaison (Jahr)")
plt.ylabel("Anzahl der Nächtigungen")
plt.xticks(x_years[::2], rotation=45)
plt.grid(True)
plt.savefig("data/innsbruck_land_plot.png")

# 3.1
df["min"] = df.iloc[:, 3:].min(axis=1)
df["max"] = df.iloc[:, 3:].max(axis=1)
df["range"] = df["max"] - df["min"]
df["mean"] = df.iloc[:, 3:].mean(axis=1)
df["std"] = df.iloc[:, 3:].std(axis=1)
df["standardized_range"] = df["range"] / df["std"]

print("\nStatistiken pro Gemeinde:")
print(
    df[["Gemeinde", "min", "max", "range", "mean", "std", "standardized_range"]].head()
)

# 3.2
total_tourists_per_year = df.iloc[:, 3:].sum(axis=0)

total_tourists_all_years = total_tourists_per_year.sum()

sum_bez = df.groupby("Bez")[df.columns[3:]].sum()

plt.figure(figsize=(12, 6))
sum_bez.sum(axis=1).plot.bar()
plt.title("Gesamtzahl der Nächtigungen pro Bezirk")
plt.xlabel("Bezirk")
plt.ylabel("Anzahl der Nächtigungen")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/bezirk_plot.png")

# 4.1
plt.figure(figsize=(12, 8))
df.boxplot(column="standardized_range", by="Bez")
plt.title("Vergleich der standardisierten Ranges pro Bezirk")
plt.suptitle("")
plt.xlabel("Bezirk")
plt.ylabel("Standardisierte Range")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/bezirk_boxplot.png")

# 4.2
plt.figure(figsize=(12, 6))
sns.barplot(x=x_years, y=innsbruck_row, hue=x_years, palette="terrain")
plt.legend().set_visible(False)
plt.title("Jahreswerte für Innsbruck")
plt.xlabel("Jahr")
plt.ylabel("Anzahl der Nächtigungen")
plt.xticks(rotation=70)
plt.tight_layout()
plt.savefig("data/innsbruck_barplot.png")

# 5
df2: pd.DataFrame = pd.read_excel("./bev_meld.xlsx")
both = pd.merge(df, df2, how='inner', on = 'Gemnr')
both = both.drop(columns=['Gemnr', 'Gemeinde_y', 'Bezirk'])

# a.
both["tourists_per_inhabitant_2018"] = both["x2018"] / both[2018]

print("\nTouristen pro Einwohner in 2018 (erste 5 Gemeinden):")
print(both[["Gemeinde_x", "tourists_per_inhabitant_2018"]].head())

# b.
plt.figure(figsize=(12, 8))
sns.boxplot(data=both, x="Bez", y="tourists_per_inhabitant_2018")
plt.title("Touristen pro Einwohner in 2018, gruppiert nach Bezirk")
plt.xlabel("Bezirk")
plt.ylabel("Touristen pro Einwohner")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/tourists_per_inhabitant_boxplot.png")

# c.
print("\nTop 10 Gemeinden mit dem höchsten Touristen-pro-Einwohner-Verhältnis in 2018:")
top_10 = both.sort_values(by="tourists_per_inhabitant_2018", ascending=False).head(10)
print(top_10[["Gemeinde_x", "tourists_per_inhabitant_2018"]])

print("\nTop 10 Gemeinden mit dem niedrigsten Touristen-pro-Einwohner-Verhältnis in 2018:")
bottom_10 = both.sort_values(by="tourists_per_inhabitant_2018", ascending=True).head(10)
print(bottom_10[["Gemeinde_x", "tourists_per_inhabitant_2018"]])

# d.
print("\nVerhältnis für Fritzens:")
fritzens_ratio = both.loc[both['Gemeinde_x'].str.strip() == 'Fritzens', 'tourists_per_inhabitant_2018']
print(fritzens_ratio.to_string())
