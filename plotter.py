import matplotlib.pyplot as plt
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES
from conversion import convert_basic, convert_supplementary


def plot_basic_scales(raw_scores, gender, k_score):
    if len(raw_scores) != len(BASIC_SCALES):
        print(f"Expected {len(BASIC_SCALES)} scores, but received {len(raw_scores)}.")
        return

    # K correction lookup table
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

    # Apply K corrections
    corrected[3] += k_values[0]   # Scale 4 (Pd)
    corrected[6] += k_values[1]   # Scale 7 (Pt)
    corrected[9] += k_score       # Scale 10 (Mf)
    corrected[10] += k_score      # Scale 11 (Pa)
    corrected[11] += k_values[2]  # Scale 12 (Sc)

    # Convert raw scores to T-scores
    T_scores = []
    for i, raw in enumerate(corrected):
        scale_name = BASIC_SCALES[i].split("+")[0]
        T = convert_basic(scale_name, raw, gender)
        T_scores.append(T)

    # Plot
    x = list(range(len(BASIC_SCALES)))
    T_min, T_max = 30, 120
    buffer = 10

    clamped_T_scores = [t if t is not None else (T_min - buffer) for t in T_scores]

    fig, ax = plt.subplots(figsize=(16, 6))

    # Split into valid and missing
    x_valid = [xi for xi, t in zip(x, T_scores) if t is not None]
    y_valid = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is not None]
    raw_valid = [raw for raw, t in zip(corrected, T_scores) if t is not None]

    x_missing = [xi for xi, t in zip(x, T_scores) if t is None]
    y_missing = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is None]
    raw_missing = [raw for raw, t in zip(corrected, T_scores) if t is None]

    # Plot continuous line for valid points
    ax.plot(x_valid, y_valid, marker="o", color="black")

    # Overlay red dots for missing
    ax.scatter(x_missing, y_missing, color="red")

    # Add raw score labels
    for xi, yi, raw in zip(x_valid, y_valid, raw_valid):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)
    for xi, yi, raw in zip(x_missing, y_missing, raw_missing):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(BASIC_SCALES)

    ax.set_ylim(T_min - buffer, T_max)
    ax.set_yticks(range(T_min, T_max + 1, 5))

    # Secondary y-axis
    ax2 = ax.twinx()
    ax2.set_ylim(T_min - buffer, T_max)
    ax2.set_yticks(ax.get_yticks())

    # Reference lines
    ax.axhline(50, color="gray", linestyle="--")
    ax.axhline(65, color="gray", linestyle="--")
    ax.axvline(x=2.5, color="black", linewidth=3)

    # "T" labels
    ax.text(0.00, -0.03, "T", transform=ax.transAxes,
            fontsize=14, ha="center", va="top", weight="bold")
    ax2.text(1.00, -0.03, "T", transform=ax2.transAxes,
             fontsize=14, ha="center", va="top", weight="bold")

    plt.title(f"MMPI-2 {gender.capitalize()} Basic Scales (K-Corrected)")
    plt.xlabel("Scale")
    plt.tight_layout()
    plt.show()


def plot_supplementary_scales(raw_scores, gender):
    if len(raw_scores) != len(SUPPLEMENTARY_SCALES):
        print(f"Expected {len(SUPPLEMENTARY_SCALES)} scores, but received {len(raw_scores)}.")
        return

    # Convert raw scores to T-scores
    T_scores = []
    for i, raw in enumerate(raw_scores):
        scale_name = SUPPLEMENTARY_SCALES[i]
        T = convert_supplementary(scale_name, raw, gender)
        T_scores.append(T)

    # Plot
    x = list(range(len(SUPPLEMENTARY_SCALES)))
    T_min, T_max = 30, 120
    buffer = 10

    clamped_T_scores = [t if t is not None else (T_min - buffer) for t in T_scores]

    fig, ax = plt.subplots(figsize=(18, 6))

    # Split into valid and missing
    x_valid = [xi for xi, t in zip(x, T_scores) if t is not None]
    y_valid = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is not None]
    raw_valid = [raw for raw, t in zip(raw_scores, T_scores) if t is not None]

    x_missing = [xi for xi, t in zip(x, T_scores) if t is None]
    y_missing = [yi for yi, t in zip(clamped_T_scores, T_scores) if t is None]
    raw_missing = [raw for raw, t in zip(raw_scores, T_scores) if t is None]

    # Plot continuous line for valid points
    ax.plot(x_valid, y_valid, marker="o", color="black")

    # Overlay red dots for missing
    ax.scatter(x_missing, y_missing, color="red")

    # Add raw score labels
    for xi, yi, raw in zip(x_valid, y_valid, raw_valid):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)
    for xi, yi, raw in zip(x_missing, y_missing, raw_missing):
        ax.text(xi, yi + 1, f"{raw}", ha="center", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(SUPPLEMENTARY_SCALES)

    ax.set_ylim(T_min - buffer, T_max)
    ax.set_yticks(range(T_min, T_max + 1, 5))

    # Secondary y-axis
    ax2 = ax.twinx()
    ax2.set_ylim(T_min - buffer, T_max)
    ax2.set_yticks(ax.get_yticks())

    # Reference lines
    ax.axhline(50, color="gray", linestyle="--")
    ax.axhline(65, color="gray", linestyle="--")

    ax.text(0.00, -0.03, "T", transform=ax.transAxes,
            fontsize=14, ha="center", va="top", weight="bold")
    ax2.text(1.00, -0.03, "T", transform=ax2.transAxes,
             fontsize=14, ha="center", va="top", weight="bold")

    plt.title(f"MMPI-2 {gender.capitalize()} Supplementary Scales")
    plt.xlabel("Scale")
    plt.tight_layout()
    plt.show()

