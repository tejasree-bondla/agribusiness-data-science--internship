import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week-3/data/agribusiness_cleaned.csv")

print("========== DATASET INFO ==========")
print(df.info())
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df[["Area_Ha", "Production_Tonnes", "Yield_Tonnes_Per_Ha"]].describe())

crop = df.groupby("Crop", as_index=False).agg(
    Area_Ha=("Area_Ha", "sum"),
    Production_Tonnes=("Production_Tonnes", "sum"),
    Yield_Tonnes_Per_Ha=("Yield_Tonnes_Per_Ha", "mean")
)

season = df.groupby("Season", as_index=False).agg(
    Area_Ha=("Area_Ha", "sum"),
    Production_Tonnes=("Production_Tonnes", "sum"),
    Yield_Tonnes_Per_Ha=("Yield_Tonnes_Per_Ha", "mean")
)

print("\n========== CROP SUMMARY ==========")
print(crop)
print("\n========== SEASON SUMMARY ==========")
print(season)

plt.figure(figsize=(8,5))
plt.bar(crop["Crop"], crop["Production_Tonnes"])
plt.title("Production by Crop")
plt.xlabel("Crop")
plt.ylabel("Production (Tonnes)")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("Week-3/visualizations/production_by_crop.png", dpi=180)
plt.close()

plt.figure(figsize=(8,5))
plt.bar(crop["Crop"], crop["Yield_Tonnes_Per_Ha"])
plt.title("Average Yield by Crop")
plt.xlabel("Crop")
plt.ylabel("Yield (Tonnes per Hectare)")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("Week-3/visualizations/yield_by_crop.png", dpi=180)
plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["Area_Ha"], df["Production_Tonnes"], s=90)
for _, row in df.iterrows():
    plt.annotate(row["Crop"], (row["Area_Ha"], row["Production_Tonnes"]),
                 xytext=(5, 5), textcoords="offset points")
plt.title("Area vs Production")
plt.xlabel("Area (Hectares)")
plt.ylabel("Production (Tonnes)")
plt.tight_layout()
plt.savefig("Week-3/visualizations/area_vs_production.png", dpi=180)
plt.close()

plt.figure(figsize=(7,5))
plt.bar(season["Season"], season["Production_Tonnes"])
plt.title("Production by Season")
plt.xlabel("Season")
plt.ylabel("Production (Tonnes)")
plt.tight_layout()
plt.savefig("Week-3/visualizations/production_by_season.png", dpi=180)
plt.close()

print("\nEDA completed. Charts saved in Week-3/visualizations/")
