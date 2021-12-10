import csv
data = [{
    'Song': 'Abba',
    'Year': '1977',

}, {
    'Song': 'BonnyM',
    'Year': '1980',

}, {
    'Song': 'Modern Talking',
    'Year': '1977',

}, {
    'Song': 'Pesnyaru',
    'Year': '1982',

}, {
    'Song': 'ACDC',
    'Year': '1983',

}, {
    'Song': 'Scorpions',
    'Year': '1984',

}]

with open('csv_write_songs.csv', 'w') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

print("csv_write_songs.csv")

with open("csv_write_songs.csv") as r_file:
    file_reader = csv.DictReader(r_file, delimiter = ",")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'{", ".join(row)}')
        print(f' {row["Song"]}  {row["Year"]}')
        count += 1
