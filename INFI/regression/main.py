import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_excel("./data/bev_meld.xlsx")

year_cols = [col for col in df.columns if isinstance(col, int)]
years = np.array(year_cols)

def analyze_and_predict(y_values, name, ax=None):
    X = sm.add_constant(years) 
    y = y_values.values
    
    model = sm.OLS(y, X).fit()
    
    b = model.params[0] 
    a = model.params[1]
    
    pred_2030_manual = a * 2030 + b
    
    future_years = np.arange(2030, 2101)
    X_future = sm.add_constant(future_years)
    predictions_future = model.predict(X_future)
    
    print(f"--- Analysis for {name} ---")
    print(f"Model: y = {a:.2f} * x + {b:.2f}")
    print(f"R² (Fit Quality): {model.rsquared:.4f}")
    print(f"Prognose 2030 (Manual): {pred_2030_manual:.0f}")
    print(f"Prognose 2100 (Model): {predictions_future[-1]:.0f}\n")

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(years, y, color='blue', label='Tatsächliche Werte')
    
    ax.plot(years, model.predict(X), color='red', label=f'Regression (a={a:.2f})')
    
    ax.set_title(f"Bevölkerungsentwicklung: {name}")
    ax.set_xlabel("Jahr")
    ax.set_ylabel("Bevölkerung")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    
    return model, a

tirol_total = df[year_cols].sum()
analyze_and_predict(tirol_total, "Tirol Gesamt")
plt.savefig("./out/tirol_regression.png")

my_community_name = "Innsbruck" 
my_community_data = df[df["Gemeinde"].str.strip() == my_community_name][year_cols].iloc[0]

analyze_and_predict(my_community_data, my_community_name)
plt.savefig("./out/gemeinde_regression.png")

bez_1_code = "IL"
bez_2_code = "RE"

bez_1_data = df[df["Bezirk"] == bez_1_code][year_cols].sum()
bez_2_data = df[df["Bezirk"] == bez_2_code][year_cols].sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

model_1, slope_1 = analyze_and_predict(bez_1_data, f"Bezirk {bez_1_code}", ax=ax1)
model_2, slope_2 = analyze_and_predict(bez_2_data, f"Bezirk {bez_2_code}", ax=ax2)

plt.tight_layout()
plt.savefig("./out/bezirks_vergleich.png")

print(f"Steigungsvergleich: {bez_1_code}: {slope_1:.2f} vs {bez_2_code}: {slope_2:.2f}")
