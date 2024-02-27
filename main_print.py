import os
import random
import pickle
import cups

last_printed_file = None

def print_random_file(printer_name, files_to_print):
    global last_printed_file

    if last_printed_file in files_to_print:
        files_to_print.remove(last_printed_file)
        files_to_print.append(last_printed_file)

    random.shuffle(files_to_print)

    if files_to_print:
        next_file = files_to_print[0]

        conn = cups.Connection()
        printers = conn.getPrinters()

        if printer_name in printers:
            printer_id = printer_name
            options = {"raw": ""}
            content = f"%%cpi:{12}\n%%lpi:{8}\n"
            content = content.encode('utf-8')
            conn.printFile(printer_id, next_file, "My Document", options)
            last_printed_file = next_file
        else:
            print(f"Imprimante '{printer_name}' non trouvée.")
    else:
        print("Tous les fichiers ont déjà été imprimés.")
