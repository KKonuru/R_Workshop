import csv

# Input CSV file with semicolons as separators
input_file = 'gliders.csv'
# Output CSV file with commas as separators
output_file = 'glider.csv'

# Open the input CSV file for reading
with open(input_file, 'r', newline='') as input_csv_file:
    # Open the output CSV file for writing
    with open(output_file, 'w', newline='') as output_csv_file:
        # Create a CSV reader using semicolon as the delimiter
        csv_reader = csv.reader(input_csv_file, delimiter=';')
        # Create a CSV writer using comma as the delimiter
        csv_writer = csv.writer(output_csv_file, delimiter=',')

        # Iterate through the input rows and write to the output file
        for row in csv_reader:
            csv_writer.writerow(row)

print(f'CSV file "{input_file}" has been converted and saved as "{output_file}".')