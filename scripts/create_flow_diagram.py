import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ---------- Figure setup ----------
fig, ax = plt.subplots(figsize=(14, 7.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis("off")

# ---------- Style ----------
BG = "white"
BOX_FILL = "#F6F8FB"
BOX_EDGE = "#2F5D7E"
TITLE = "#16324F"
TEXT = "#2B2B2B"
ARROW = "#4A6C86"
SUBBOX_FILL = "#EDF3F8"

fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# ---------- Helpers ----------
def rounded_box(x, y, w, h, title, lines, title_size=12, text_size=9,
                fill=BOX_FILL, edge=BOX_EDGE, lw=1.8, align="left"):
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.03,rounding_size=0.12",
        linewidth=lw,
        edgecolor=edge,
        facecolor=fill
    )
    ax.add_patch(box)

    # title
    ax.text(
        x + 0.22, y + h - 0.28, title,
        ha="left", va="top",
        fontsize=title_size, fontweight="bold", color=TITLE
    )

    # divider
    ax.plot([x + 0.18, x + w - 0.18], [y + h - 0.48, y + h - 0.48],
            color=edge, lw=1)

    # body text
    start_y = y + h - 0.72
    line_gap = 0.28
    for i, line in enumerate(lines):
        if align == "left":
            tx = x + 0.22
            ha = "left"
        else:
            tx = x + w / 2
            ha = "center"

        ax.text(
            tx, start_y - i * line_gap, line,
            ha=ha, va="top",
            fontsize=text_size, color=TEXT
        )

def arrow(x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            lw=2,
            color=ARROW,
            shrinkA=5,
            shrinkB=5,
            mutation_scale=14
        )
    )

# ---------- Title ----------
ax.text(
    7, 7.65,
    "Study Design and Analytical Pipeline",
    ha="center", va="top",
    fontsize=18, fontweight="bold", color=TITLE
)
ax.text(
    7, 7.3,
    "Gjöll fire fatality study",
    ha="center", va="top",
    fontsize=10.5, color="#5A6B7A"
)

# ---------- Main flow boxes ----------
rounded_box(
    0.6, 4.5, 2.9, 2.0,
    "1. Data Sources",
    [
        "• Newspaper archives (Timarit.is)",
        "• Institutional yearbooks",
        "• Government reports",
        "• Court records",
    ],
)

rounded_box(
    4.0, 4.85, 2.4, 1.3,
    "2. Verification",
    [
        "• Cross-checked against",
        "  ≥2 independent sources",
        "• 113 incidents verified",
    ],
)

rounded_box(
    6.9, 4.35, 3.0, 2.3,
    "3. Gjöll Registry",
    [
        "• 113 fatal incidents",
        "• 145 deaths (1968–2025)",
        "• 93 structure fires",
        "• 20 other incidents",
        "• Construction year and location",
    ],
)

# Analysis parent box
analysis_outer = patches.FancyBboxPatch(
    (10.4, 2.0), 3.0, 4.65,
    boxstyle="round,pad=0.03,rounding_size=0.12",
    linewidth=1.8,
    edgecolor=BOX_EDGE,
    facecolor=BOX_FILL
)
ax.add_patch(analysis_outer)

ax.text(
    10.62, 6.45, "4. Analysis",
    ha="left", va="top",
    fontsize=12, fontweight="bold", color=TITLE
)
ax.plot([10.58, 13.22], [6.2, 6.2], color=BOX_EDGE, lw=1)

# Descriptive sub-box
desc = patches.FancyBboxPatch(
    (10.65, 4.15), 2.5, 1.7,
    boxstyle="round,pad=0.02,rounding_size=0.08",
    linewidth=1.2,
    edgecolor=BOX_EDGE,
    facecolor=SUBBOX_FILL
)
ax.add_patch(desc)
ax.text(10.82, 5.65, "Descriptive", ha="left", va="top",
        fontsize=10.5, fontweight="bold", color=TITLE)
for i, t in enumerate([
    "• Incident severity and burden",
    "• Decade-aggregated trends",
    "• Seasonal patterns (Oct–Mar)",
    "• Construction-year distribution",
]):
    ax.text(10.82, 5.38 - i * 0.26, t, ha="left", va="top",
            fontsize=8.6, color=TEXT)

# Inferential sub-box
inf = patches.FancyBboxPatch(
    (10.65, 2.35), 2.5, 1.45,
    boxstyle="round,pad=0.02,rounding_size=0.08",
    linewidth=1.2,
    edgecolor=BOX_EDGE,
    facecolor=SUBBOX_FILL
)
ax.add_patch(inf)
ax.text(10.82, 3.62, "Inferential", ha="left", va="top",
        fontsize=10.5, fontweight="bold", color=TITLE)
for i, t in enumerate([
    "• Person-years exposure (pre/post-1998)",
    "• Sensitivity: missing construction year",
    "• ITSA: Poisson segmented regression",
    "• Negative binomial robustness check",
]):
    ax.text(10.82, 3.35 - i * 0.24, t, ha="left", va="top",
            fontsize=8.4, color=TEXT)

# ---------- Arrows ----------
arrow(3.5, 5.5, 4.0, 5.5)    # Data sources -> Verification
arrow(6.4, 5.5, 6.9, 5.5)    # Verification -> Registry
arrow(9.9, 5.5, 10.4, 5.5)   # Registry -> Analysis

# ---------- Save ----------
plt.tight_layout()
plt.savefig(
    "figures/fig5_methodology_flow_improved.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=BG
)
print("Saved to figures/fig5_methodology_flow_improved.png")
plt.show()