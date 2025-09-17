from tkinter import messagebox
from plotter import plot_basic_scales, plot_supplementary_scales
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES

def submit_data(name, age, location, date, gender, k_score, basic_entries, supp_entries):
    basic_scores = {}
    supp_scores = {}
     
    # Validate client age
    if not str(age).isdigit():
        messagebox.showerror("Invalid input",f"{age} is not a valid age.")
        return

    # Validate k_score
    if not str(k_score).isdigit():
        messagebox.showerror("Invalid input", "K-Score must be an integer.")
        return
    if not int(k_score) >= 0 and int(k_score) <= 30:
        messagebox.showerror("Invalid input", "Please enter a K-Score between 0 and 30.")
        return
    k_score = int(k_score)

    # Validate basic scale inputs
    for scale, var in basic_entries.items():
        value = var.get().strip()
        if not value.isdigit():
            messagebox.showerror("Invalid Input", f"Basic scale '{scale}' must be an integer.")
            return
        basic_scores[scale] = int(value)

    # Validate supplementary scale inputs
    for scale, var in supp_entries.items():
        value = var.get().strip()
        if not value.isdigit():
            messagebox.showerror("Invalid Input", f"Supplementary scale '{scale}' must be an integer.")
            return
        supp_scores[scale] = int(value)
 
    # Debug print
    print("Client Info:")
    print(f" Name: {name}, Age: {age}, Location: {location}, Date: {date}, Gender: {gender}, K-Score: {k_score}\n")
    print("Basic Scores:", basic_scores)
    print("Supplementary Scores:", supp_scores)

    # Convert to lists and plot
    raw_basic_scores = [basic_scores[scale] for scale in BASIC_SCALES]
    plot_basic_scales(raw_basic_scores, gender, k_score)

    raw_supp_scores = [supp_scores[scale] for scale in SUPPLEMENTARY_SCALES]
    plot_supplementary_scales(raw_supp_scores, gender)


    # TODO: printing/exporting can go here
    # e.g., save to PDF, generate report, etc.

