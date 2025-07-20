import matplotlib.pyplot as plt

# ------ BASIC SCALES GRAPH -------

def basic_scales(scores_page1, Kscore, gender):

    # Array of scales for page 1
    scales_page1 = ["L", "F", "K", "Hc+.5K", "D", "Hy", "Pd+.4K", "Mf", "Pa", "Pl+.4k", "Sc+1K", "Ma+.2K", "Si"]

    # Dictionary for K-Factors
    k_lookup = { 
        0: [0, 0, 0],
        1: [1, 0, 0],
        2: [1, 1, 0],
        3: [2, 1, 1],
        4: [2, 2, 1],
        5: [3, 2, 1],
        6: [3, 2, 1],
        7: [4, 3, 1],
        8: [4, 3, 2],
        9: [5, 4, 2],
        10: [5, 4, 2],
        11: [6, 4, 2],
        12: [6, 5, 2],
        13: [7, 5, 3],
        14: [7, 6, 3],
        15: [8, 6, 3],
        16: [8, 6, 3],
        17: [9, 7, 3],
        18: [9, 7, 4],
        19: [10, 8, 4],
        20: [10, 8, 4],
        21: [11, 8, 4],
        22: [11, 9, 4],
        23: [12, 9, 5],
        24: [12, 10, 5],
        25: [13, 10, 5],
        26: [13, 10, 5],
        27: [14, 11, 5],
        28: [14, 11, 6],
        29: [15, 12, 6],
        30: [15, 12, 6]
    }

    # Check for correct amount of inputs
    if len(scores_page1) != len(scales_page1):
        print(f"Expected {len(scales_page1)} scores, but got {len(scores_page1)}.")
        return

    # Add the fraction of k or k itself to the corresponding scale's raw score
    k_values = k_lookup.get(Kscore, [0, 0, 0])

    corrected_scores = scores_page1.copy()
    corrected_scores[3] += k_values[0]  # Hc
    corrected_scores[6] += k_values[1]  # Pd
    corrected_scores[9] += Kscore       # Pl
    corrected_scores[10] += Kscore      # Sc
    corrected_scores[11] += k_values[2] # Ma

    # X positions for L, F, and K
    x1 = [0, 1, 2]
    y1 = corrected_scores[0:3]

    # X positions for Hc-Si
    x2 = list(range(3, len(scales_page1)))
    y2 = corrected_scores[3:]

    # Set figure size and plot points
    fig, ax = plt.subplots(figsize=(16, 5))
    
    # L, F, and K
    ax.plot(x1, y1, marker = 'o', linestyle = '-', color = 'black')
    
    # Hc - Si
    ax.plot(x2, y2, marker = 'o', linestyle = '-', color = 'black')

    # Bold vertical separator for "L, F, K"
    ax.axvline(x = 2.5, color = 'black', linewidth = 3)
    
    # Add point labels above each point
    for i, y in zip(x1, y1):
        ax.text(i, y + 1, str(int(y)), ha = 'center', fontsize = 8)
    for i, y in zip(x2, y2):
        ax.text(i, y + 1, str(int(y)), ha = 'center', fontsize = 8)

    # X axis labels
    ax.set_xticks(range(len(scales_page1)))
    ax.set_xticklabels(scales_page1)
   
    # T scale on represented on left and right. Left:
    T_min, T_max = 30, 120
    buffer = 10
    ax.set_ylim(T_min - buffer, T_max)
    ax.set_yticks(range(T_min, T_max + 1, 5))
    ax.text(0, -0.02, "T", transform = ax.transAxes, fontsize = 12, ha = 'center', va = 'top')
    
    # Adding T scale to right side
    ax2 = ax.twinx()
    ax2.set_ylim(T_min - buffer, T_max)
    ax2.set_yticks(ax.get_yticks())
    ax2.text(1.0, -0.02, "T", transform = ax.transAxes, fontsize = 12, ha = 'center', va = 'top')

    # T scale reference lines
    ax.axhline(y = 50, color = 'gray', linestyle = '--')
    ax.axhline(y = 65, color = 'gray', linestyle = '--')

    # Titles and finish creating
    title = f"MMPI-2 {gender} K-Corrected"
    plt.title(title)
    plt.xlabel("Scale")
    plt.ylabel("")

    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)

    plt.tight_layout()
    plt.show()


# ------ SUPPLEMENTARY SCALES GRAPH ------

def supplementary_scales(scores_page2, gender):

    # Array of 19 scales for page 2
    scales_page2 = ["A", "R", "Es", "MAC-R", "AAS",  "APS", "MDS", "O-H", "Do", "Re", "Mt", "GM", "GF", "PK",  "PS",  "Si1", "Si2", "Si3", "F3"]
    
    # Check for correct amount
    if len(scores_page2) != len(scales_page2):
        print(f"Expected {len(scales_page2)} scores, but got {len(scores_page2)}.")  
        return
    
    # Set figure size and plot points
    fig, ax = plt.subplots(figsize = (18, 8))
    ax.plot(scales_page2, scores_page2, marker='o', linestyle = '-', color = 'black')
        
    # Add labels above each point
    for i, score in enumerate(scores_page2):
        ax.text(i, score + 2, str(int(score)), ha='center', fontsize=9)
    
    # X axis labels
    ax.set_xticks(range(len(scales_page2)))
    ax.set_xticklabels(scales_page2)
   
    # T scale on represented on left and right. Left:
    T_min, T_max = 30, 120
    buffer = 10
    ax.set_ylim(T_min - buffer, T_max)
    ax.set_yticks(range(T_min, T_max + 1, 5))
    ax.text(0, -0.02, "T", transform = ax.transAxes, fontsize = 12, ha = 'center', va = 'top')
    
    # Adding T scale to right side
    ax2 = ax.twinx()
    ax2.set_ylim(T_min - buffer, T_max)
    ax2.set_yticks(ax.get_yticks())
    ax2.text(1.0, -0.02, "T", transform = ax.transAxes, fontsize = 12, ha = 'center', va = 'top')

    # T scale reference lines
    ax.axhline(y = 50, color = 'gray', linestyle = '--')
    ax.axhline(y = 65, color = 'gray', linestyle = '--')

    # Titles and finish creating
    title = f"MMPI-2 {gender} K-Corrected"
    plt.title(title)
    plt.xlabel("Scale")
    plt.ylabel("")

    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)

    plt.tight_layout()
    plt.show()


