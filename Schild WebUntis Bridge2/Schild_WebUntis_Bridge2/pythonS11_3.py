import os
import csv
from datetime import datetime

def run(use_abschlussdatum=True, create_second_file=True):
    print(f'Inside your_script.py - use_abschlussdatum: {use_abschlussdatum}')  # Debug print
    # Create subdirectory if it doesn't exist
    if not os.path.exists('WebUntis Importe'):
        os.makedirs('WebUntis Importe')

    # Find the newest CSV file in the current directory
    newest_file = max([f for f in os.listdir('.') if f.endswith('.csv')], key=os.path.getctime)

    # Set output file name with current date and time
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f'WebUntis Importe/WebUntis Import {now}.csv'
    second_output_file = f'WebUntis Importe/WebUntis Import {now}_Fehlende Entlassdatum.csv'

    # Define columns to filter for
    columns_to_filter = ['Interne ID-Nummer', 'Nachname', 'Vorname', 'Geburtsdatum', 'Klasse', 'Geschlecht', 'Entlassdatum', 'Aufnahmedatum', 'vorauss. Abschlussdatum', 'Schulpflicht erfüllt', 'Volljährig', 'E-Mail (privat)', 'Telefon-Nr.', 'Fax-Nr.', 'Straße', 'Postleitzahl', 'Ortsname']

    # Define columns for output file
    output_columns = ['Interne ID-Nummer', 'Nachname', 'Vorname', 'Geburtsdatum', 'Klasse', 'Geschlecht', 'Entlassdatum', 'Aufnahmedatum', 'vorauss. Abschlussdatum', 'Schulpflicht', 'Volljährig', 'E-Mail (privat)', 'Telefon-Nr.', 'Fax-Nr.', 'Straße', 'Postleitzahl', 'Ortsname', 'Aktiv']
    second_output_columns = ['Interne ID-Nummer', 'Klasse', 'Nachname', 'Vorname', 'Geburtsdatum']

    # Extract data from input file
    output_data = []
    with open(newest_file, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        header = [column for column in reader.fieldnames if column in columns_to_filter]
        header.append('Schulpflicht')
        header.append('Aktiv')
        output_data.append(output_columns)
        for row in reader:
            filtered_row = {k: v for k, v in row.items() if k in columns_to_filter}
            # Switch 'Ja' for 'Nein' and vice versa due to Schulpflicht vs. Schulpflicht erfüllt 
            if 'Schulpflicht erfüllt' in filtered_row:
                if filtered_row['Schulpflicht erfüllt'] == 'Ja':
                    filtered_row['Schulpflicht'] = 'Nein'
                elif filtered_row['Schulpflicht erfüllt'] == 'Nein':
                    filtered_row['Schulpflicht'] = 'Ja'
            # Check for valid dates and use the earlier date as Entlassdatum
            entlassdatum = filtered_row.get('Entlassdatum', '')
            abschlussdatum = filtered_row.get('vorauss. Abschlussdatum', '')
            if entlassdatum and abschlussdatum:
                try:
                    entlassdatum_date = datetime.strptime(entlassdatum, '%d.%m.%Y')
                    abschlussdatum_date = datetime.strptime(abschlussdatum, '%d.%m.%Y')
                    if use_abschlussdatum and abschlussdatum_date < entlassdatum_date:
                        entlassdatum = abschlussdatum
                except ValueError:
                    pass
            elif not entlassdatum and abschlussdatum and use_abschlussdatum:
                entlassdatum = abschlussdatum
            filtered_row['Entlassdatum'] = entlassdatum
            # Check for active pupils
            if 'Status' in row:
                if row['Status'] == '2':
                    filtered_row['Aktiv'] = 'Ja'
                else:
                    filtered_row['Aktiv'] = 'Nein'
            output_data.append([filtered_row.get(col, '') for col in output_columns])

    # Extract data for second output file
    second_output_data = []
    with open(newest_file, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        header = [column for column in reader.fieldnames if column in columns_to_filter]
        for row in reader:
            if row['Status'] != '2' and not row.get('Entlassdatum'):
                filtered_row = {k: v for k, v in row.items() if k in second_output_columns}
                second_output_data.append([filtered_row.get(col, '') for col in second_output_columns])

    # Write filtered data to output file
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(output_data)

    print(f'Done. Output file name: {output_file}')

    # Write second output file
    if create_second_file:
        with open(second_output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(second_output_columns)
            writer.writerows(second_output_data)

        print(f'Second output file name: {second_output_file}')