import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("./hypothesen/ESS8e02.1_F1.csv", sep=",", low_memory=False)

df["gndr_label"] = pd.cut(
    df["gndr"], [0, 1, 2, 9], labels=["Male", "Female", "No Answer"]
)

sns.set_theme(style="whitegrid")

print("Daten geladen. Zeilen:", len(df))

data_a = df[df["gndr"].isin([1, 2])].dropna(subset=["trstplc"])

group_male = data_a[data_a["gndr"] == 1]["trstplc"]
group_female = data_a[data_a["gndr"] == 2]["trstplc"]

plt.figure(figsize=(8, 6))
sns.boxplot(x="gndr_label", y="trstplc", data=data_a, palette="Set2")
plt.title("Vertrauen in die Polizei nach Geschlecht")
plt.ylabel("Vertrauen (0-10)")
plt.savefig("./hypothesen/polizei.png")

stat, p_val = stats.mannwhitneyu(group_male, group_female, alternative="greater")

print(f"Hypothese A - Mann-Whitney-U: Statistik={stat}, p-Wert={p_val}")

data_b = df[["elgnuc", "elgsun"]].dropna()

plt.figure(figsize=(8, 6))
ct = pd.crosstab(data_b["elgnuc"], data_b["elgsun"])
sns.heatmap(ct, annot=True, fmt="d", cmap="viridis")
plt.title("Zusammenhalt Atomstrom vs. Solarstrom")
plt.xlabel("Solarstrom Zustimmung")
plt.ylabel("Atomstrom Zustimmung")
plt.show()

corr, p_val = stats.spearmanr(data_b["elgnuc"], data_b["elgsun"])

print(f"Hypothese B - Spearman Korrelation: r={corr}, p-Wert={p_val}")

data_c = df[df["cntry"].isin(["AT", "HU"])].dropna(subset=["ccgdbd"])

group_at = data_c[data_c["cntry"] == "AT"]["ccgdbd"]
group_hu = data_c[data_c["cntry"] == "HU"]["ccgdbd"]

plt.figure(figsize=(8, 6))
sns.violinplot(x="cntry", y="ccgdbd", data=data_c, palette="muted")
plt.title("Wahrnehmung Auswirkungen Klimawandel (AT vs HU)")
plt.ylabel("0 = Sehr schlecht ... 10 = Sehr gut")
plt.savefig("./hypothesen/klimawandel.png")

stat, p_val = stats.mannwhitneyu(group_at, group_hu, alternative="less")

print(f"Hypothese C - Mann-Whitney-U: Statistik={stat}, p-Wert={p_val}")

data_d = df[df["gndr"].isin([1, 2])].dropna(subset=["basinc"])

group_m = data_d[data_d["gndr"] == 1]["basinc"]
group_f = data_d[data_d["gndr"] == 2]["basinc"]

plt.figure(figsize=(8, 6))
sns.countplot(x="basinc", hue="gndr_label", data=data_d)
plt.title("Zustimmung Grundeinkommen (1=Stark dafür, 4=Stark dagegen)")
plt.savefig("./hypothesen/grundeinkommen.png")

stat, p_val = stats.mannwhitneyu(group_f, group_m, alternative="less")

print(f"Hypothese D - Mann-Whitney-U: Statistik={stat}, p-Wert={p_val}")

data_e1 = df[["happy", "health"]].dropna()

sns.jointplot(x="happy", y="health", data=data_e1, kind="hex")
plt.savefig("./hypothesen/happyhealth.png")

corr_e1, p_e1 = stats.spearmanr(data_e1["happy"], data_e1["health"])
print(f"Eigene 1 - Spearman: r={corr_e1}, p={p_e1}")

data_e2 = df[["yrbrn", "netustm"]].dropna()

corr_e2, p_e2 = stats.spearmanr(data_e2["yrbrn"], data_e2["netustm"])
print(f"Eigene 2 - Spearman: r={corr_e2}, p={p_e2}")
