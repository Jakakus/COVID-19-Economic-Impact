"""
COVID-19 Economic Impact Analysis on Businesses
------------------------------------------------
Project Overview:
• Problem: Analyze the impact of COVID-19 on business revenues.
• Data Source: Synthetic data generated within this script.
• Methods:
    - Data Simulation: Generate data for 1,000 businesses, including pre-COVID revenue,
      post-COVID revenue (after a drop factor), and compute revenue decline percentages.
    - Data Analysis & Visualization: Create a histogram of revenue decline, a boxplot
      by business sector, a bar plot for average decline per sector, and a scatter plot
      comparing pre- and post-COVID revenues.
    - Image Export: Save all generated plots as PNG images in the "output_images" folder.
• Tools: Python (Pandas, NumPy, Matplotlib, Seaborn)
• How to Run:
    1. Install required packages:
         pip install pandas numpy matplotlib seaborn
    2. Run the script:
         python covid_impact_analysis.py
    3. Open the "output_images" folder to access the downloadable images.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Set Up Environment ---
np.random.seed(42)  # For reproducibility

# Create output directory if it does not exist
output_dir = "output_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")

# --- Data Simulation ---
n_businesses = 1000
sectors = ["Retail", "Hospitality", "Manufacturing", "Services", "Healthcare"]

# Generate synthetic business data
business_ids = np.arange(1, n_businesses + 1)
business_sectors = np.random.choice(sectors, size=n_businesses)

# Simulate pre-COVID revenue (in thousands of dollars)
pre_covid_revenue = np.random.normal(loc=500, scale=150, size=n_businesses)
pre_covid_revenue = np.clip(pre_covid_revenue, 100, None)  # Ensure revenue is at least 100

# Simulate revenue drop factor between 0.3 and 1.0 for post-COVID revenue
drop_factors = np.random.uniform(low=0.3, high=1.0, size=n_businesses)
post_covid_revenue = pre_covid_revenue * drop_factors

# Create DataFrame
df = pd.DataFrame({
    "business_id": business_ids,
    "sector": business_sectors,
    "pre_covid_revenue": pre_covid_revenue,
    "post_covid_revenue": post_covid_revenue
})

# Compute revenue decline percentage
df["decline_percent"] = ((df["pre_covid_revenue"] - df["post_covid_revenue"]) /
                         df["pre_covid_revenue"]) * 100

# Save data summary for reference
csv_path = os.path.join(output_dir, "covid_impact_data.csv")
df.to_csv(csv_path, index=False)
print(f"Data saved to: {csv_path}")

# --- Data Visualization ---

# Plot 1: Histogram of Revenue Decline Percentages
plt.figure(figsize=(10, 6))
sns.histplot(df["decline_percent"], bins=30, kde=True, color="skyblue")
plt.title("Histogram of Revenue Decline Percentages")
plt.xlabel("Revenue Decline (%)")
plt.ylabel("Count")
hist_path = os.path.join(output_dir, "hist_decline_percent.png")
plt.savefig(hist_path)
plt.close()
print(f"Histogram saved to: {hist_path}")

# Plot 2: Boxplot of Revenue Decline by Sector
plt.figure(figsize=(10, 6))
sns.boxplot(x="sector", y="decline_percent", data=df, palette="Set3")
plt.title("Revenue Decline Percentage by Sector")
plt.xlabel("Sector")
plt.ylabel("Revenue Decline (%)")
boxplot_path = os.path.join(output_dir, "boxplot_decline_by_sector.png")
plt.savefig(boxplot_path)
plt.close()
print(f"Boxplot saved to: {boxplot_path}")

# Plot 3: Bar Plot of Average Revenue Decline by Sector
avg_decline = df.groupby("sector")["decline_percent"].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x="sector", y="decline_percent", data=avg_decline, palette="viridis")
plt.title("Average Revenue Decline Percentage by Sector")
plt.xlabel("Sector")
plt.ylabel("Average Revenue Decline (%)")
barplot_path = os.path.join(output_dir, "barplot_avg_decline_by_sector.png")
plt.savefig(barplot_path)
plt.close()
print(f"Bar plot saved to: {barplot_path}")

# Plot 4: Scatter Plot of Pre-COVID vs. Post-COVID Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x="pre_covid_revenue", y="post_covid_revenue", hue="sector",
                data=df, alpha=0.7, palette="deep")
# Plot the reference line for "No Change"
max_rev = df["pre_covid_revenue"].max()
plt.plot([0, max_rev], [0, max_rev], 'r--', label="No Change")
plt.title("Pre-COVID vs. Post-COVID Revenue")
plt.xlabel("Pre-COVID Revenue (thousands)")
plt.ylabel("Post-COVID Revenue (thousands)")
plt.legend()
scatter_path = os.path.join(output_dir, "scatter_pre_vs_post_revenue.png")
plt.savefig(scatter_path)
plt.close()
print(f"Scatter plot saved to: {scatter_path}")

print("All images have been saved in the 'output_images' folder. You can now download them from that folder.")
