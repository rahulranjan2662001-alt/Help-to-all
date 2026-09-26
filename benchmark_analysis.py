import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "solar_manufacturers.csv"
OUTPUT = Path(__file__).resolve().parents[1] / "analysis" / "output"
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

# Convert numeric columns where available.
df["module_capacity_gw"] = pd.to_numeric(df["module_capacity_gw"], errors="coerce")
df["max_module_efficiency_pct"] = pd.to_numeric(df["max_module_efficiency_pct"], errors="coerce")

# Capacity chart: only verified/populated values are plotted.
plot_df = df.dropna(subset=["module_capacity_gw"]).sort_values("module_capacity_gw")

if not plot_df.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(plot_df["company"], plot_df["module_capacity_gw"])
    plt.xlabel("Module manufacturing capacity (GW)")
    plt.ylabel("Company")
    plt.title("Solar PV Module Manufacturing Capacity")
    plt.tight_layout()
    plt.savefig(OUTPUT / "module_capacity.png", dpi=200)
    plt.close()

print("Analysis complete.")
print(df.to_string(index=False))
