"""Figure 1 — Study design and analytical pipeline (Gjöll registry).

Vertical 4-stage flow authored at final column width (6.3 in) so LaTeX
includes it at 100% with no downscaling. Matplotlib Agg only.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# ---------------------------------------------------------------- palette ---
NAVY = "#1b3a5b"      # headers, edges, arrows
SLATE = "#33475e"     # body text
FILL = "#f4f7fa"      # box fill
HEADER_FILL = "#e3eaf2"
WHITE = "#ffffff"

# ------------------------------------------------------------------ canvas --
FIG_W, FIG_H = 6.3, 5.75          # inches — authored at true display size
FIG = Path(__file__).resolve().parents[1] / "figures" / "fig_study_design.png"

MARGIN = 0.28                     # outer margin (in)
BOX_W = FIG_W - 2 * MARGIN
GAP = 0.34                        # vertical gap between boxes (arrow lives here)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "text.color": SLATE,
})

fig = plt.figure(figsize=(FIG_W, FIG_H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.set_axis_off()

# ------------------------------------------------------------------ helpers -
HEADER_H = 0.30                   # header band height (in)


def stage_box(y_top, box_h, number, title, draw_body):
    """Rounded stage box with a tinted header band; body drawn by callback."""
    x = MARGIN
    y = y_top - box_h
    ax.add_patch(FancyBboxPatch(
        (x, y), BOX_W, box_h,
        boxstyle="round,pad=0,rounding_size=0.07",
        linewidth=1.1, edgecolor=NAVY, facecolor=FILL, zorder=2))
    # header band (drawn slightly inset so the rounded corners stay clean)
    ax.add_patch(FancyBboxPatch(
        (x + 0.035, y_top - HEADER_H), BOX_W - 0.07, HEADER_H - 0.035,
        boxstyle="round,pad=0,rounding_size=0.045",
        linewidth=0, facecolor=HEADER_FILL, zorder=3))
    ax.text(x + 0.16, y_top - HEADER_H / 2 - 0.017,
            f"{number}", ha="left", va="center",
            fontsize=9.5, fontweight="bold", color=NAVY, zorder=4)
    ax.text(x + 0.42, y_top - HEADER_H / 2 - 0.017,
            title, ha="left", va="center",
            fontsize=9.5, fontweight="bold", color=NAVY, zorder=4)
    draw_body(x, y, y_top)
    return y                       # bottom edge


def bullets(lines, x0, y0, fontsize=8.3, leading=0.185):
    for i, line in enumerate(lines):
        ax.text(x0, y0 - i * leading, "•", ha="left", va="top",
                fontsize=fontsize, color=NAVY, zorder=4)
        ax.text(x0 + 0.14, y0 - i * leading, line, ha="left", va="top",
                fontsize=fontsize, color=SLATE, zorder=4)


def down_arrow(y_from, y_to):
    ax.add_patch(FancyArrowPatch(
        (FIG_W / 2, y_from - 0.03), (FIG_W / 2, y_to + 0.03),
        arrowstyle="-|>", mutation_scale=13,
        linewidth=1.4, color=NAVY, zorder=1))


# ------------------------------------------------------------------- title --
y = FIG_H - 0.16
ax.text(FIG_W / 2, y, "Study design and analytical pipeline",
        ha="center", va="top", fontsize=10.5, fontweight="bold", color=NAVY)
y -= 0.42

# --------------------------------------------------------- stage 1: sources -
def body1(x, y_bot, y_top):
    ytxt = y_top - HEADER_H - 0.10
    col2 = x + BOX_W / 2 + 0.10
    bullets(["Newspaper archives (Tímarit.is)",
             "Institutional yearbooks"], x + 0.16, ytxt)
    bullets(["Government investigation reports",
             "Court records"], col2, ytxt)

y = stage_box(y, HEADER_H + 0.60, "1", "Data sources", body1)
down_arrow(y, y - GAP); y -= GAP

# ---------------------------------------------------- stage 2: verification -
def body2(x, y_bot, y_top):
    ytxt = y_top - HEADER_H - 0.10
    bullets(["Each incident cross-checked against ≥ 2 independent sources",
             "113 fatal incidents verified for inclusion"], x + 0.16, ytxt)

y = stage_box(y, HEADER_H + 0.60, "2", "Verification", body2)
down_arrow(y, y - GAP); y -= GAP

# -------------------------------------------------------- stage 3: registry -
def body3(x, y_bot, y_top):
    ytxt = y_top - HEADER_H - 0.10
    col2 = x + BOX_W / 2 + 0.10
    bullets(["113 fatal incidents, 145 deaths (1968–2025)",
             "93 structure fires; 20 other fire-related"], x + 0.16, ytxt)
    bullets(["Construction year of building",
             "Incident location"], col2, ytxt)

y = stage_box(y, HEADER_H + 0.60, "3", "Gjöll registry", body3)
down_arrow(y, y - GAP); y -= GAP

# -------------------------------------------------------- stage 4: analysis -
def body4(x, y_bot, y_top):
    ytxt = y_top - HEADER_H - 0.10
    col2 = x + BOX_W / 2 + 0.10
    ax.text(x + 0.16, ytxt, "Descriptive", fontsize=8.3,
            fontweight="bold", color=NAVY, ha="left", va="top", zorder=4)
    bullets(["Severity and decade trends",
             "Seasonality; cohort patterns"], x + 0.16, ytxt - 0.20)
    ax.text(col2, ytxt, "Inferential", fontsize=8.3,
            fontweight="bold", color=NAVY, ha="left", va="top", zorder=4)
    bullets(["Person-years; exact Poisson rate ratios",
             "Segmented ITSA with robustness checks"], col2, ytxt - 0.20)

y = stage_box(y, HEADER_H + 0.82, "4", "Analysis", body4)

fig.savefig(FIG, dpi=300, facecolor=WHITE)
plt.close(fig)
print(f"Saved {FIG}")
