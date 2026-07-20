#!/usr/bin/env python3
"""Generate the study-design / analytical-pipeline schematic (Figure 1).

Produces figures/fig_study_design.png — a clean four-stage pipeline
(Sources -> Verification -> Gjoll registry -> Analysis) for the Fire
Technology manuscript. Requested by co-author T. Barry (review rounds 1 & 2).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

NAVY = "#1b3a5b"
FILL = "#f4f7fa"
EDGE = "#1b3a5b"

FIG = Path(__file__).resolve().parents[1] / "figures" / "fig_study_design.png"

stages = [
    ("1. Data sources", [
        "Newspaper archives (Tímarit.is)",
        "Institutional yearbooks",
        "Government investigation reports",
        "Court records",
    ]),
    ("2. Verification", [
        "Cross-checked against",
        "≥2 independent sources",
        "where available",
        "113 incidents verified",
    ]),
    ("3. Gjöll registry", [
        "113 fatal incidents",
        "145 deaths (1968–2025)",
        "93 structure fires",
        "20 other fire-related",
        "Construction year & location",
    ]),
    ("4. Analysis", [
        "Descriptive: severity, decade",
        "trends, seasonality, cohort",
        "Inferential: person-years,",
        "exact Poisson rate ratios,",
        "segmented ITSA + robustness",
    ]),
]

fig, ax = plt.subplots(figsize=(11, 3.6), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 34)
ax.axis("off")

n = len(stages)
box_w = 20.5
gap = (100 - n * box_w) / (n + 1)
y0, box_h = 5, 22
centers = []
for i, (title, items) in enumerate(stages):
    x = gap + i * (box_w + gap)
    centers.append((x, x + box_w))
    ax.add_patch(FancyBboxPatch(
        (x, y0), box_w, box_h,
        boxstyle="round,pad=0.3,rounding_size=1.2",
        linewidth=1.4, edgecolor=EDGE, facecolor=FILL))
    ax.text(x + box_w / 2, y0 + box_h - 2.6, title, ha="center", va="center",
            fontsize=11, fontweight="bold", color=NAVY)
    ax.plot([x + 1.5, x + box_w - 1.5], [y0 + box_h - 4.8] * 2,
            color=NAVY, linewidth=0.8)
    for j, item in enumerate(items):
        ax.text(x + 1.4, y0 + box_h - 6.8 - j * 2.9, "• " + item,
                ha="left", va="center", fontsize=8, color="#22303c")

for (l, r), (nl, nr) in zip(centers[:-1], centers[1:]):
    ax.add_patch(FancyArrowPatch(
        (r + 0.4, y0 + box_h / 2), (nl - 0.4, y0 + box_h / 2),
        arrowstyle="-|>", mutation_scale=16, linewidth=1.6, color=NAVY))

ax.text(50, 31.5, "Study design and analytical pipeline",
        ha="center", va="center", fontsize=13, fontweight="bold", color=NAVY)

fig.savefig(FIG, bbox_inches="tight", facecolor="white")
print(f"wrote {FIG}")
