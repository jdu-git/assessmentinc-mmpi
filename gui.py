import tkinter as tk
from tkinter import ttk
from datetime import datetime
from norms import BASIC_SCALES, SUPPLEMENTARY_SCALES
from handlers import submit_data

def main():
    # Create root window
    root = tk.Tk()
    root.title("MMPI-2 T-Score Plotter")
    root.geometry("900x700")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)

    # Title
    title_label = ttk.Label(frame, text="MMPI-2 Scale Entry", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=8, pady=10, sticky="we")

    # ----- Client Info Section -----
    ttk.Label(frame, text="Client Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    client_name = tk.StringVar()
    ttk.Entry(frame, textvariable=client_name, width=25).grid(row=1, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="Client Age:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
    client_age = tk.IntVar()
    ttk.Entry(frame, textvariable=client_age, width=5).grid(row=1, column=3, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="Testing Company:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    client_test_location = tk.StringVar()
    ttk.Entry(frame, textvariable=client_test_location, width=25).grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Date Tested
    ttk.Label(frame, text="Date Tested:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    month_var = tk.StringVar(value=str(datetime.now().month))
    ttk.Combobox(frame, textvariable=month_var, values=[str(i) for i in range(1, 13)], width=3).grid(row=3, column=1)
    day_var = tk.StringVar(value=str(datetime.now().day))
    ttk.Combobox(frame, textvariable=day_var, values=[str(i) for i in range(1, 32)], width=3).grid(row=3, column=2)
    year_var = tk.StringVar(value=str(datetime.now().year))
    ttk.Combobox(frame, textvariable=year_var, values=[str(i) for i in range(2020, 2031)], width=5).grid(row=3, column=3)

    # Gender
    ttk.Label(frame, text="Gender:").grid(row=1, column=4, padx=5, pady=5, sticky="w")
    client_gender = tk.StringVar(value="female")
    ttk.Combobox(frame, textvariable=client_gender, values=["male", "female"], width=7).grid(row=1, column=5)

    # K Score
    ttk.Label(frame, text="K Score:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
    client_k_score = tk.StringVar()
    ttk.Entry(frame, textvariable=client_k_score, width=5).grid(row=5, column=1, padx=5, pady=5)

    # Basic Scales
    basic_entries = {}
    num_columns = 2
    start_row = 7
    for i, scale in enumerate(BASIC_SCALES):
        row = start_row + i // num_columns
        col = (i % num_columns) * 2
        ttk.Label(frame, text=scale).grid(row=row, column=col, sticky="w", padx=5, pady=2)
        var = tk.StringVar()
        ttk.Entry(frame, textvariable=var, width=5).grid(row=row, column=col+1, padx=5, pady=2)
        basic_entries[scale] = var

    # Supplementary Scales
    supp_entries = {}
    supp_start_row = start_row + (len(BASIC_SCALES) // num_columns) + 2
    for i, scale in enumerate(SUPPLEMENTARY_SCALES):
        row = supp_start_row + i // num_columns
        col = (i % num_columns) * 2
        ttk.Label(frame, text=scale).grid(row=row, column=col, sticky="w", padx=5, pady=2)
        var = tk.StringVar()
        ttk.Entry(frame, textvariable=var, width=5).grid(row=row, column=col+1, padx=5, pady=2)
        supp_entries[scale] = var

    # Submit button calls submit_data from handlers.py
    submit_button = ttk.Button(
        frame, text="Submit",
        command=lambda: submit_data(
            client_name.get(),
            client_age.get(),
            client_test_location.get(),
            f"{month_var.get()}/{day_var.get()}/{year_var.get()}",
            client_gender.get(),
            client_k_score.get(),
            basic_entries,
            supp_entries
        )
    )
    submit_button.grid(row=999, column=0, columnspan=4, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()

