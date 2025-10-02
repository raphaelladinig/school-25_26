import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./data/wetter_hohe_warte.csv", sep=";")

df.columns = [col.replace("_", "") for col in df.columns]

# 2

df["MONTH"] = df["REFDATE"] % 100
month_counts = df["MONTH"].value_counts().sort_index()
print("\nAnzahl der Einträge pro Monat:")
print(month_counts)

min_year = df["REFYEAR"].min()
max_year = df["REFYEAR"].max()
print(f"\nÄltestes Jahr im Datensatz: {min_year}")
print(f"Aktuellstes Jahr im Datensatz: {max_year}")

print("\nStatistiken für wichtige Variablen:")
wichtige_variablen = ["T", "NUMFROST", "NUMSUMMER"]
for var in wichtige_variablen:
    min_val = df[var].min()
    max_val = df[var].max()
    print(f"Variable '{var}': Min = {min_val}, Max = {max_val}")

print("\nAnzahl der fehlenden Werte (NaN) pro wichtiger Variable:")
for var in wichtige_variablen:
    nan_count = df[var].isnull().sum()
    print(f"Variable '{var}': {nan_count} NaN-Werte")

# 2.1

years_to_plot = [1880, 1950, 1990, 2020]

data_for_boxplot = []
for year in years_to_plot:
    temp_data_array = df[df["REFYEAR"] == year]["T"]

    cleaned_data = temp_data_array[np.isfinite(temp_data_array)]
    data_for_boxplot.append(cleaned_data)

plt.figure(figsize=(10, 6))
plt.boxplot(data_for_boxplot, tick_labels=[str(y) for y in years_to_plot])
plt.title("Vergleich der täglichen Durchschnittstemperaturen über ausgewählte Jahre")
plt.xlabel("Jahr")
plt.ylabel("Tägliche Durchschnittstemperatur in °C")
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("out/temperaturunterschiede_boxplot")

# 2.2

july_df = df[df["MONTH"] == 7]

plt.figure(figsize=(12, 6))
plt.scatter(july_df["REFYEAR"], july_df["T"], alpha=0.6, s=10)
plt.title("Durchschnittstemperatur im Juli (1872 - heute)")
plt.xlabel("Jahr")
plt.ylabel("Durchschnittstemperatur im Juli in °C")

z = np.polyfit(july_df["REFYEAR"], july_df["T"], 1)
p = np.poly1d(z)
plt.plot(july_df["REFYEAR"], p(july_df["REFYEAR"]), "r--", label="Trendlinie")
plt.legend()

plt.grid(True)
plt.savefig("out/durchschnittstemperatur_juli.png")

for month in range(1, 13):
    month_df = df[df["MONTH"] == month]

    if not month_df.empty:
        plt.figure(figsize=(10, 5))
        plt.scatter(month_df["REFYEAR"], month_df["T"], alpha=0.5, s=10)
        plt.title(f"Durchschnittstemperatur im Monat {month}")
        plt.xlabel("Jahr")
        plt.ylabel("Temperatur in °C")
        plt.grid(True)
        plt.savefig(f"out/temperatur_monat_{month}.png")


yearly_summary = (
    df.groupby("REFYEAR")
    .agg({"NUMHEAT": "sum", "NUMFROST": "sum", "NUMWINDVEL60": "sum"})
    .reset_index()
)

plt.figure(figsize=(12, 6))
plt.plot(yearly_summary["REFYEAR"], yearly_summary["NUMHEAT"], label="Anzahl Hitzetage")
plt.title("Jährliche Anzahl der Hitzetage (Tmax >= 30°C)")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Tage")
plt.grid(True)
plt.legend()
plt.savefig("out/hitzetage.png")

plt.figure(figsize=(12, 6))
plt.plot(
    yearly_summary["REFYEAR"], yearly_summary["NUMFROST"], label="Anzahl Frosttage"
)
plt.title("Jährliche Anzahl der Frosttage (Tmin < 0°C)")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Tage")
plt.grid(True)
plt.legend()
plt.savefig("out/frosttage.png")

plt.figure(figsize=(12, 6))
plt.plot(
    yearly_summary["REFYEAR"], yearly_summary["NUMWINDVEL60"], label="Anzahl Windtage"
)
plt.title("Jährliche Anzahl der Windtage")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Tage")
plt.grid(True)
plt.legend()
plt.savefig("out/windtage.png")

# 2.3

variable_zum_vergleich = "MEANTMAX"
fruehe_periode_start = 1900
fruehe_periode_ende = 1929
rezente_periode_start = 1995
rezente_periode_ende = df["REFYEAR"].max() - 1  # z.B. 2024

label_frueh = f"{fruehe_periode_start}-{fruehe_periode_ende}"
label_rezent = f"{rezente_periode_start}-{rezente_periode_ende}"

maske_frueh = (df["REFYEAR"] >= fruehe_periode_start) & (
    df["REFYEAR"] <= fruehe_periode_ende
)
daten_frueh = df.loc[maske_frueh, variable_zum_vergleich].dropna()

maske_rezent = (df["REFYEAR"] >= rezente_periode_start) & (
    df["REFYEAR"] <= rezente_periode_ende
)
daten_rezent = df.loc[maske_rezent, variable_zum_vergleich].dropna()

daten_fuer_plot = [daten_frueh, daten_rezent]

plt.figure(figsize=(10, 7))
plt.boxplot(daten_fuer_plot)

plt.title(f"Vergleich der Verteilung von: {variable_zum_vergleich}", fontsize=16)
plt.ylabel("Mittleres tägliches Maximum der Lufttemperatur in °C", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig("out/boxplot.png")

# 2.3

variable_zum_vergleich = 'MEANTMAX'
fruehe_periode_start = 1900
fruehe_periode_ende = 1929
rezente_periode_start = 1995
rezente_periode_ende = df['REFYEAR'].max() # Bis zum aktuellsten Jahr

label_frueh = f"Frühe Periode ({fruehe_periode_start}-{fruehe_periode_ende})"
label_rezent = f"Rezente Periode ({rezente_periode_start}-{rezente_periode_ende})"

# Daten filtern und NaNs entfernen
maske_frueh = (df['REFYEAR'] >= fruehe_periode_start) & (df['REFYEAR'] <= fruehe_periode_ende)
daten_frueh = df.loc[maske_frueh, variable_zum_vergleich].dropna()

maske_rezent = (df['REFYEAR'] >= rezente_periode_start) & (df['REFYEAR'] <= rezente_periode_ende)
daten_rezent = df.loc[maske_rezent, variable_zum_vergleich].dropna()

daten_fuer_plot = [daten_frueh, daten_rezent]

plt.figure(figsize=(10, 7))
plt.boxplot(daten_fuer_plot, tick_labels=[label_frueh, label_rezent])

plt.title(f'Vergleich der Verteilung von: {variable_zum_vergleich}', fontsize=16)
plt.ylabel('Mittleres tägliches Maximum der Lufttemperatur in °C', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("out/boxplot_vergleich_perioden.png")

# 2.4

jahre = yearly_summary["REFYEAR"].values
frosttage_pro_jahr = yearly_summary["NUMFROST"].to_numpy()

sort_idx_frost = np.argsort(frosttage_pro_jahr)[::-1]

print("\nTop 5 Jahre mit den meisten Frosttagen:")
for i in range(5):
    idx = sort_idx_frost[i]
    jahr = jahre[idx]
    wert = frosttage_pro_jahr[idx]
    print(f"{i+1}. Jahr {jahr} mit {int(wert)} Frosttagen")
