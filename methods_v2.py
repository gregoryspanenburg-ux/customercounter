from pandas import read_excel
from calendar import month_name
import tkinter as tk
from tkinter.filedialog import askopenfilename

TYPE = "abonnement - type"
MONTH = "month"
HOUR = "hour"

def input_console(message):
    return input(message)

def choose_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file = askopenfilename(
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    root.destroy()
    return file

def print_console(message):
    print(">", message)

def prepare_file(file_string):
    # inlezen
    file = read_excel(file_string)

    # Nodige kolommen eruit filteren
    file = file[['abonnement - Verbruik', 'abonnement - type', 'abonnement - verbruiken']]

    # Cellen met lege types verwijderen
    file = file.dropna(subset=[TYPE])
    file[TYPE] = file[TYPE].str.lower()

    # Datum + tijdstip verwijderen
    verbruik_split = file['abonnement - Verbruik'].str.split(" ")
    file[MONTH] = verbruik_split.str[0].str.split("-").str[1]
    file[HOUR] = verbruik_split.str[1]
    file = file.drop(["abonnement - Verbruik"], axis=1)

    return file


def get_all_swimming_customers(file):
    return file[file[TYPE].str.contains("aqua|zwembad|individueel ticket|groepstarief")]


def get_all_fitness_customers(file):
    return file[file[TYPE].str.contains("fitness|move slim")]

def generate_datatable_of_morning_hours(file_with_morning):
    file_with_morning = file_with_morning.groupby(MONTH, as_index=False).sum().iloc[:, 0:3:2]

    file_with_morning[MONTH] = file_with_morning[MONTH].astype(int)
    file_with_morning[MONTH] = file_with_morning[MONTH].map(month_name.__getitem__)

    file_with_morning = file_with_morning.rename(columns={
        "month": "Maand",
        "abonnement - verbruiken": "Aantal bezoekers",
    })

    return file_with_morning

def get_morning_hours_file(hours, file):
    return file[file[HOUR].str.contains(f"^0[{hours}]:*", regex=True)]


def print_table_header(title):
    full_line = ("=" * 4) + ( "=" * len(title) )
    print()
    print()
    print()
    print(full_line)
    print(f"= {title} =")
    print(full_line)
    print()
