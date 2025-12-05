"""
Customer Analytics: Purchase Amount Distribution by Customer Segment

This script:
- Generates realistic synthetic customer purchase data
- Creates a Seaborn boxplot of purchase amount by customer segment
- Styles the plot for executive-ready presentations
- Saves the chart as chart.png with 512x512 pixel dimensions

Author contact: 23f2001336@ds.study.iitm.ac.in
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_synthetic_data(random_state: int = 42) -> pd.DataFrame:
    """
    Generate realistic synthetic purchase amount data
    for different customer segments.

    Segments:
    - Budget: lower spend, lower variance
    - Regular: medium spend, moderate variance
    - Premium: higher spend, higher variance
    - VIP: very high spend, more variability and outliers

    Returns:
        DataFrame with columns: ['Segment', 'PurchaseAmount']
    """
    rng = np.random.default_rng(random_state)

    segments = []
    amounts = []

    # Budget segment: smaller purchases
    n_budget = 200
    segments += ["Budget"] * n_budget
    amounts += list(rng.normal(loc=25, scale=8, size=n_budget).clip(min=5))

    # Regular segment: middle of the distribution
    n_regular = 250
    segments += ["Regular"] * n_regular
    amounts += list(rng.normal(loc=60, scale=15, size=n_regular).clip(min=10))

    # Premium segment: higher spending customers
    n_premium = 180
    segments += ["Premium"] * n_premium
    amounts += list(rng.normal(loc=120, scale=25, size=n_premium).clip(min=20))

    # VIP segment: very high spenders with more variance and some big outliers
    n_vip = 120
    segments += ["VIP"] * n_vip
    base_vip = rng.normal(loc=220, scale=40, size=n_vip).clip(min=50)
    # Add a few extreme outliers
    outlier_indices = rng.choice(n_vip, size=5, replace=False)
    base_vip[outlier_indices] *= rng.uniform(1.8, 2.5, size=5)
    amounts += list(base_vip)

    df = pd.DataFrame(
        {
            "Segment": segments,
            "PurchaseAmount": amounts,
        }
    )

    return df


def create_boxplot(df: pd.DataFrame, output_path: str = "chart.png") -> None:
    """
    Create a Seaborn boxplot of purchase amount by customer segment
    and save it as a 512x512 PNG.

    Uses:
    - sns.boxplot for visualization
    - Professional styling (style, context, palette)
    """
    # Professional Seaborn styling
    sns.set_style("whitegrid")
    sns.set_context("talk")  # good sizing for presentations

    # 512x512 pixels: figsize (inches) * dpi = pixels → 8 * 64 = 512
    plt.figure(figsize=(8, 8))

    # Sort segments in a logical spending order
    order = ["Budget", "Regular", "Premium", "VIP"]

    ax = sns.boxplot(
        data=df,
        x="Segment",
        y="PurchaseAmount",
        order=order,
        palette="Set2",
        showfliers=True,
    )

    # Titles and labels
    ax.set_title(
        "Purchase Amount Distribution by Customer Segment",
        pad=20,
        fontsize=18,
        weight="bold",
    )
    ax.set_xlabel("Customer Segment", fontsize=14)
    ax.set_ylabel("Purchase Amount ($)", fontsize=14)

    # Make y-axis a bit roomier
    ymin, ymax = df["PurchaseAmount"].min(), df["PurchaseAmount"].max()
    plt.ylim(ymin * 0.9, ymax * 1.1)

    # Improve layout
    plt.tight_layout()

    # Save exactly 512x512 pixels
    plt.savefig(output_path, dpi=64, bbox_inches="tight")
    plt.close()


def main() -> None:
    """
    Main entry point:
    - Generate data
    - Create and save the boxplot
    """
    df = generate_synthetic_data()
    create_boxplot(df, output_path="chart.png")


if __name__ == "__main__":
    main()
