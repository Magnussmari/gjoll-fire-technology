"""
Generate a methodology flow diagram for the Gjöll fire fatality study.
Shows: Data Sources → Verification → Gjöll Registry → Analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis("off")

# Colors
box_color = "#E8EDF2"
arrow_color = "#2C3E50"
header_color = "#1E3A5F"
text_color = "#333333"

def draw_box(ax, x, y, w, h, title, items, title_color=header_color):
    rect = mpatches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.1",
        facecolor=box_color,
        edgecolor=header_color,
        linewidth=1.5,
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h - 0.25, title,
        ha="center", va="top",
        fontsize=10, fontweight="bold", color=title_color,
    )
    for i, item in enumerate(items):
        ax.text(
            x + w / 2, y + h - 0.6 - i * 0.3, item,
            ha="center", va="top",
            fontsize=8, color=text_color,
        )

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->,head_width=0.3,head_length=0.15",
            color=arrow_color,
            lw=1.5,
        ),
    )

# Box 1: Data Sources (left)
draw_box(ax, 0.3, 4.2, 2.2, 2.4, "Data Sources", [
    "Newspaper archives",
    "(Timarit.is)",
    "Institutional yearbooks",
    "Government reports",
    "Court records",
])

# Box 2: Verification (center-left)
draw_box(ax, 3.3, 4.7, 2.0, 1.4, "Verification", [
    "Cross-checked against",
    "≥2 independent sources",
    "(113 incidents verified)",
])

# Box 3: Gjöll Registry (center-right)
draw_box(ax, 6.1, 4.2, 2.2, 2.4, "Gjöll Registry", [
    "113 fatal incidents",
    "145 deaths (1968–2025)",
    "93 structure fires",
    "20 other incidents",
    "Construction year, location",
])

# Box 4: Analysis (right) — split into two sub-boxes
# Descriptive
draw_box(ax, 0.3, 0.8, 3.8, 2.6, "Descriptive Analysis", [
    "Incident severity and burden",
    "Decade-aggregated trends",
    "Seasonal patterns (Oct–Mar)",
    "Construction-year distribution",
    "Non-structure incident patterns",
])

# Inferential
draw_box(ax, 5.0, 0.8, 4.2, 2.6, "Inferential Analysis", [
    "Person-years exposure (pre/post-1998)",
    "Sensitivity: missing construction year",
    "ITSA: Poisson segmented regression",
    "Negative binomial robustness check",
    "Exact Poisson confidence bounds",
])

# Arrows
# Sources → Verification
draw_arrow(ax, 2.5, 5.4, 3.3, 5.4)
# Verification → Registry
draw_arrow(ax, 5.3, 5.4, 6.1, 5.4)
# Registry → Descriptive
draw_arrow(ax, 6.8, 4.2, 2.2, 3.4)
# Registry → Inferential
draw_arrow(ax, 7.6, 4.2, 7.1, 3.4)

# Title
ax.text(
    5.0, 6.7,
    "Study Design and Analytical Pipeline",
    ha="center", va="top",
    fontsize=13, fontweight="bold", color=header_color,
)

plt.tight_layout()
plt.savefig(
    "figures/fig5_methodology_flow.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
)
print("Flow diagram saved to figures/fig5_methodology_flow.png")
