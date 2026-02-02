print("Loading packages...")

from time import sleep
from methods_v2 import *

print("===============================================")
print("Sportoase Ochtend Klant teller")
print("===============================================")
input_console("Start? (enter)")

running = True

try:
    while running:
        print_console("Kies een bestand...")
        file_path = choose_file()
        print_console("Bestand voorbereiden (dit kan even duren)...")
        file = prepare_file(file_path)

        print()
        print()

        print_console("Bezoekers aan het tellen...")
        file_all_aqua = get_all_swimming_customers(file)
        file_all_fitness = get_all_fitness_customers(file)

        print_console("Bezoekers aan het opsplitsen...")

        file_aqua_six_to_seven = get_morning_hours_file("456", file_all_aqua)
        file_aqua_seven_to_eight = get_morning_hours_file("7", file_all_aqua)

        file_fitness_six_to_seven = get_morning_hours_file("456", file_all_fitness)
        file_fitness_seven_to_eight = get_morning_hours_file("7", file_all_fitness)

        print_console("Tabellen genereren...")

        dt_aqua_six_to_seven = generate_datatable_of_morning_hours(file_aqua_six_to_seven)
        dt_aqua_seven_to_eight = generate_datatable_of_morning_hours(file_aqua_seven_to_eight)

        dt_fitness_six_to_seven = generate_datatable_of_morning_hours(file_fitness_six_to_seven)
        dt_fitness_seven_to_eight = generate_datatable_of_morning_hours(file_fitness_seven_to_eight)

        print_console("Tabellen weergeven:")

        print_table_header("Aqua: bezoekers tussen 06u00 - 07u00")
        print(dt_aqua_six_to_seven)

        print_table_header("Aqua: bezoekers tussen 07u00 - 08u00")
        print(dt_aqua_seven_to_eight)

        print_table_header("Fitness: bezoekers tussen 06u00 - 07u00")
        print(dt_fitness_six_to_seven)

        print_table_header("Fitness: bezoekers tussen 07u00 - 08u00")
        print(dt_fitness_seven_to_eight)

        print()
        print()
        running = False

    input_console("beëindig script? (enter)")
    print_console("Bye bye :/")
    sleep(1)
except Exception as e:
    print()
    print("=" * 50)
    print_console("ERROR OPGETREDEN :(")
    print("=" * 50)
    print(f"\nError type: {type(e).__name__}")
    print(f"Error boodschap: {str(e)}")
    print("\nVolledige traceback:")
    print("-" * 50)
    print("-" * 50)
    print()
    input_console("Druk op enter om te sluiten...")