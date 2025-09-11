# main.py

from plotter import plot_basic_scales, plot_supplementary_scales
from conversion import convert_basic, convert_supplementary
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES

def main():
    # Example raw scores for testing:
    # One big list: basic + supp
    raw_scores = [
        # ---- BASIC ---- (should match length of BASIC_SCALES)
        5, 10, 12, 16, 26, 16, 18, 44, 15, 23, 20, 11, 24,  
        # ---- SUPPLEMENTARY ---- (should match length of SUPPLEMENTARY_SCALES)
        9, 14, 12, 8, 7, 20, 10, 13, 11, 10, 12, 7, 8, 9, 10, 11, 9, 8, 7
    ]

    gender = "male"   # or "female"
    Kscore = 10       # or whatever valid K you want

    # Split them:
    basic_raw = raw_scores[:len(BASIC_SCALES)]
    supp_raw = raw_scores[len(BASIC_SCALES):]

    # Plot basic
    plot_basic_scales(basic_raw, gender, Kscore, convert_basic)

    # Plot supplementary
    plot_supplementary_scales(supp_raw, gender, convert_supplementary)


if __name__ == "__main__":
    main()
