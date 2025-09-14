from plotter import plot_basic_scales, plot_supplementary_scales
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES

def submit_data(name, age, location, date, gender, k_score, basic_entries, supp_entries):
    # Convert entry dicts (StringVars) into numbers
    basic_scores = {}
    for scale, var in basic_entries.items():
        value = var.get().strip()
        basic_scores[scale] = int(value) if value.isdigit() else None

    supp_scores = {}
    for scale, var in supp_entries.items():
        value = var.get().strip()
        supp_scores[scale] = int(value) if value.isdigit() else None

    # Debug print
    print("Client Info:")
    print(f" Name: {name}, Age: {age}, Location: {location}, Date: {date}, Gender: {gender}, K-Score: {k_score}\n")
    print("Basic Scores:", basic_scores)
    print("Supplementary Scores:", supp_scores)

    # Convert to list, call plotting functions
    raw_basic_scores = [basic_scores[scale] for scale in BASIC_SCALES]
    plot_basic_scales(raw_basic_scores, gender, k_score)

    raw_supp_scores = [supp_scores[scale] for scale in SUPPLEMENTARY_SCALES]
    plot_supplementary_scales(supp_scores, gender)

    # TODO: printing/exporting can go here
    # e.g., save to PDF, generate report, etc.

