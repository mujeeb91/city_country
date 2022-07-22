import csv


INPUT_CITIES_FILEPATH = 'cities.csv'
OUTPUT_CITIES_FILEPATH = 'non_us_cities.csv'

def get_city_country(filepath):
    new_rows = []
    with open(filepath) as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        for row in csv_reader:
            country_name = row['country_name']
            if country_name != 'United States':
                new_row = [row['name'], country_name]
                new_rows.append(new_row)
    return new_rows

def save_file(filepath, rows):
    with open(filepath, 'w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        header_row = ['name', 'country_name']
        csv_writer.writerow(header_row)
        for row in rows:
            csv_writer.writerow(row)

def main():
    cities = get_city_country(INPUT_CITIES_FILEPATH)
    save_file(OUTPUT_CITIES_FILEPATH, cities)

main()