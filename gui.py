import tkinter as tk
from tkinter import ttk
from datetime import datetime
from conversion import convert_basic, convert_supplementary
from plotter import plot_basic_scales, plot_supplementary_scales
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES

# create root (window) and frame to fill it
root = tk.Tk()
root.title("MMPI-2 T-Score Plotter")
root.geometry("900x700")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Title spanning 4 columns
title_label = ttk.Label(frame, text="MMPI-2 Scale Entry", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=8, pady=10, sticky="we")  # span all columns

# ----- Client Info Section -----
# Client Name
ttk.Label(frame, text="Client Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
client_name = tk.StringVar(value="Alexis Dupuis")
ttk.Entry(frame, textvariable=client_name, width=25).grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Client Age
ttk.Label(frame, text="Client Age:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
client_age = tk.IntVar(value=18)
ttk.Entry(frame, textvariable=client_age, width=5).grid(row=1, column=3, padx=5, pady=5, sticky="w")

# Testing Company
ttk.Label(frame, text="Testing Company:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
client_test_location = tk.StringVar(value="Cleet")
ttk.Entry(frame, textvariable=client_test_location, width=25).grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Date Tested (Dropdowns)
ttk.Label(frame, text="Date Tested:").grid(row=3, column=0, padx=5, pady=5, sticky="w")

# Month
month_var = tk.StringVar()
month_cb = ttk.Combobox(frame, textvariable=month_var, values=[str(i) for i in range(1, 13)], width=3)
month_cb.grid(row=3, column=1, padx=2, pady=5, sticky="w")
month_cb.set(str(datetime.now().month))

# Day
day_var = tk.StringVar()
day_cb = ttk.Combobox(frame, textvariable=day_var, values=[str(i) for i in range(1, 32)], width=3)
day_cb.grid(row=3, column=2, padx=2, pady=5, sticky="w")
day_cb.set(str(datetime.now().day))

# Year
year_var = tk.StringVar()
year_cb = ttk.Combobox(frame, textvariable=year_var, values=[str(i) for i in range(2020, 2031)], width=5)
year_cb.grid(row=3, column=3, padx=2, pady=5, sticky="w")
year_cb.set(str(datetime.now().year))

# Gender
ttk.Label(frame, text="Gender:").grid(row=1, column=4, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar(value="female")
gender_cb = ttk.Combobox(frame, textvariable=gender_var, values=["male", "female"], width=7)
gender_cb.grid(row=1, column=5, padx=5, pady=5, sticky="w")

# Basic Scales. order: scale score scale score
basic_entries = {}
num_columns = 2
start_row = 5

for i, scale in enumerate(BASIC_SCALES):
    row = start_row + i // num_columns
    col = (i % num_columns) * 2

    ttk.Label(frame, text=scale).grid(row=row, column=col, sticky="w", padx=5, pady=2)

    var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=var, width=5)
    entry.grid(row=row, column=col+1, padx=5, pady=2)
    basic_entries[scale] = var  # store StringVar, not the widget

# Supplementary Scales same row-column orientation
supp_entries = {}
supp_start_row = start_row + (len(BASIC_SCALES) // num_columns) + 2  # space them out

for i, scale in enumerate(SUPPLEMENTARY_SCALES):
    row = supp_start_row + i // num_columns
    col = (i % num_columns) * 2

    ttk.Label(frame, text=scale).grid(row=row, column=col, sticky="w", padx=5, pady=2)

    var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=var, width=5)
    entry.grid(row=row, column=col+1, padx=5, pady=2)
    supp_entries[scale] = var
