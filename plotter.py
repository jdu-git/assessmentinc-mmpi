import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES
from conversion import convert_basic, convert_supplementary


def plot_basic_scales(raw_scores, gender, k_score, ax=None):
    """Gather all necessary data for plotting basic scales."""
    if len(raw_scores) != len(BASIC_SCALES):
        print(f"Expected {len(BASIC_SCALES)} scores, but received {len(raw_scores)}.")
        return

    k_lookup = {
        0: [0, 0, 0], 1: [1, 0, 0], 2: [1, 1, 0], 3: [2, 1, 1],
        4: [2, 2, 1], 5: [3, 2, 1], 6: [3, 2, 1], 7: [4, 3, 1],
        8: [4, 3, 2], 9: [5, 4, 2], 10: [5, 4, 2], 11: [6, 4, 2],
        12: [6, 5, 2], 13: [7, 5, 3], 14: [7, 6, 3], 15: [8, 6, 3],
        16: [8, 6, 3], 17: [9, 7, 3], 18: [9, 7, 4], 19: [10, 8, 4],
        20: [10, 8, 4], 21: [11, 8, 4], 22: [11, 9, 4], 23: [12, 9, 5],
        24: [12, 10, 5], 25: [13, 10, 5], 26: [13, 10, 5], 27: [14, 11, 5],
        28: [14, 11, 6], 29: [15, 12, 6], 30: [15, 12, 6]
    }

    corrected = raw_scores.copy()
    k_values = k_lookup.get(k_score, [0, 0, 0])

    corrected[3]  += k_values[0]
    corrected[6]  += k_values[1]
    corrected[9]  += k_score
    corrected[10] += k_score
    corrected[11] += k_values[2]

    T_scores = []
    for i, raw in enumerate(corrected):
        scale_name = BASIC_SCALES[i].split("+")[0]
        T = convert_basic(scale_name, raw, gender)
        T_scores.append(T)

    x = list(range(len(BASIC_SCALES)))
    T_min, T_max = 30, 120
    buffer = 10

    clamped_T_scores = [t if t is not None else (T_min - buffer) for t in T_scores]

    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=(16, 6))
    else:
        fig = ax.get_figure()

    x_valid   = [xi for xi, t in zip(x, T_scores) if t is not None]
    y_valid   = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is not None]
    raw_valid = [raw for raw, t in zip(corrected, T_scores) if t is not None]

    x_missing   = [xi for xi, t in zip(x, T_scores) if t is None]
    y_missing   = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is None]
    raw_missing = [raw for raw, t in zip(corrected, T_scores) if t is None]

    x_left  = [xi for xi in x_valid if xi <= 2]
    y_left  = [yi for xi, yi in zip(x_valid, y_valid) if xi <= 2]
    x_right = [xi for xi in x_valid if xi > 2]
    y_right = [yi for xi, yi in zip(x_valid, y_valid) if xi > 2]

    ax.plot(x_left,  y_left,  marker="o", color="black")
    ax.plot(x_right, y_right, marker="o", color="black")
    ax.scatter(x_missing, y_missing, color="red")

    for xi, yi, raw in zip(x_valid, y_valid, raw_valid):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)
    for xi, yi, raw in zip(x_missing, y_missing, raw_missing):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(BASIC_SCALES)
    ax.set_ylim(T_min - buffer, T_max)
    ax.set_yticks(range(T_min, T_max + 1, 5))
    ax.set_title(f"MMPI-2 {gender.capitalize()} Basic Scales (K-Corrected)")
    ax.set_xlabel("Scale")

    ax2 = ax.twinx()
    ax2.set_ylim(T_min - buffer, T_max)
    ax2.set_yticks(ax.get_yticks())

    ax.axhline(50, color="gray", linestyle="--")
    ax.axhline(65, color="gray", linestyle="--")
    ax.axvline(x=2.5, color="black", linewidth=3)

    ax.text(0.00, -0.03, "T", transform=ax.transAxes,
            fontsize=14, ha="center", va="top", weight="bold")
    ax2.text(1.00, -0.03, "T", transform=ax2.transAxes,
             fontsize=14, ha="center", va="top", weight="bold")

    if standalone:
        plt.tight_layout()
        plt.show()


def plot_supplementary_scales(raw_scores, gender, ax=None):
    """Gather all necessary for plotting supplementary scales."""
    if len(raw_scores) != len(SUPPLEMENTARY_SCALES):
        print(f"Expected {len(SUPPLEMENTARY_SCALES)} scores, but received {len(raw_scores)}.")
        return

    T_scores = []
    for i, raw in enumerate(raw_scores):
        scale_name = SUPPLEMENTARY_SCALES[i]
        T = convert_supplementary(scale_name, raw, gender)
        T_scores.append(T)

    x = list(range(len(SUPPLEMENTARY_SCALES)))
    T_min, T_max = 30, 120
    buffer = 10

    clamped_T_scores = [t if t is not None else (T_min - buffer) for t in T_scores]

    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=(18, 6))
    else:
        fig = ax.get_figure()

    x_valid   = [xi for xi, t in zip(x, T_scores) if t is not None]
    y_valid   = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is not None]
    raw_valid = [raw for raw, t in zip(raw_scores, T_scores) if t is not None]

    x_missing   = [xi for xi, t in zip(x, T_scores) if t is None]
    y_missing   = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is None]
    raw_missing = [raw for raw, t in zip(raw_scores, T_scores) if t is None]

    ax.plot(x_valid, y_valid, marker="o", color="black")
    ax.scatter(x_missing, y_missing, color="red")

    for xi, yi, raw in zip(x_valid, y_valid, raw_valid):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)
    for xi, yi, raw in zip(x_missing, y_missing, raw_missing):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(SUPPLEMENTARY_SCALES)
    ax.set_ylim(T_min - buffer, T_max)
    ax.set_yticks(range(T_min, T_max + 1, 5))
    ax.set_title(f"MMPI-2 {gender.capitalize()} Supplementary Scales")
    ax.set_xlabel("Scale")

    ax2 = ax.twinx()
    ax2.set_ylim(T_min - buffer, T_max)
    ax2.set_yticks(ax.get_yticks())

    ax.axhline(50, color="gray", linestyle="--")
    ax.axhline(65, color="gray", linestyle="--")

    ax.text(0.00, -0.03, "T", transform=ax.transAxes,
            fontsize=14, ha="center", va="top", weight="bold")
    ax2.text(1.00, -0.03, "T", transform=ax2.transAxes,
             fontsize=14, ha="center", va="top", weight="bold")

    if standalone:
        plt.tight_layout()
        plt.show()


def plot_combined_report(client_info, basic_args, supplementary_args):
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(3, 1, figure=fig, height_ratios=[0.8, 4.5, 4.5], hspace=0.6)

    # Client info block
    ax_info = fig.add_subplot(gs[0])
    ax_info.axis('off')
    info_text = (
        f"Name: {client_info['name']}    "
        f"Age: {client_info['age']}    "
        f"Gender: {client_info['gender'].capitalize()}    "
        f"Date: {client_info['date']}\n"
        f"Testing Location: {client_info['location']}"
    )
    ax_info.text(0.0, 0.6, info_text, transform=ax_info.transAxes,
                 fontsize=10, va='top', family='monospace')

    ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_subplot(gs[2])

    plot_basic_scales(*basic_args, ax=ax1)
    plot_supplementary_scales(*supplementary_args, ax=ax2)

    fig.savefig('mmpi_report.pdf', dpi=300, bbox_inches='tight')
    plt.show()
