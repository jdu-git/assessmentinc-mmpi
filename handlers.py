from tkinter import messagebox
from plotter import plot_basic_scales, plot_supplementary_scales, plot_combined_report
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES


def submit_data(name, age, location, date, gender, k_score, basic_entries, supp_entries):
    basic_scores = {}
    supp_scores = {}

    if not str(age).isdigit():
        messagebox.showerror("Invalid input", f"{age} is not a valid age.")
        return
    if not str(k_score).isdigit():
        messagebox.showerror("Invalid input", "K-Score must be an integer.")
        return
    if not int(k_score) >= 0 and int(k_score) <= 30:
        messagebox.showerror("Invalid input", "Please enter a K-Score between 0 and 30.")
        return
    k_score = int(k_score)

    for scale, var in basic_entries.items():
        value = var.get().strip()
        if not value.isdigit():
            messagebox.showerror("Invalid Input", f"Basic scale '{scale}' must be an integer.")
            return
        basic_scores[scale] = int(value)

    for scale, var in supp_entries.items():
        value = var.get().strip()
        if not value.isdigit():
            messagebox.showerror("Invalid Input", f"Supplementary scale '{scale}' must be an integer.")
            return
        supp_scores[scale] = int(value)

    raw_basic_scores = [basic_scores[scale] for scale in BASIC_SCALES]
    plot_basic_scales(raw_basic_scores, gender, k_score)
    raw_supp_scores = [supp_scores[scale] for scale in SUPPLEMENTARY_SCALES]
    plot_supplementary_scales(raw_supp_scores, gender)


def print_report(client_info, k_score, basic_entries, supp_entries):
    basic_scores = {}
    supp_scores = {}

    for scale, var in basic_entries.items():
        value = var.get().strip()
        if not value.isdigit():
            messagebox.showerror("Invalid Input", f"Basic scale '{scale}' must be an integer.")
            return
        basic_scores[scale] = int(value)

    for scale, var in supp_entries.items():
        value = var.get().strip()
        if not value.isdigit():
            messagebox.showerror("Invalid Input", f"Supplementary scale '{scale}' must be an integer.")
            return
        supp_scores[scale] = int(value)

    raw_basic_scores = [basic_scores[scale] for scale in BASIC_SCALES]
    raw_supp_scores  = [supp_scores[scale] for scale in SUPPLEMENTARY_SCALES]

    plot_combined_report(
        client_info=client_info,
        basic_args=(raw_basic_scores, client_info["gender"], int(k_score or 0)),
        supplementary_args=(raw_supp_scores, client_info["gender"])
    )


