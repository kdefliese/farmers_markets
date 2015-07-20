import csv
farmers_market = open('farmers-markets-0d51def2d3decd53415dc3b91b0253e8.csv')
csv_farmers_market = csv.reader(farmers_market)

no_space_cities = []

for row in csv_farmers_market:
  if row[31] == 'Y' and row[24] == 'N' and row[32] == 'N' and row[33] == 'N' and row[34] == 'N' and ' ' not in row[4]:
    no_space_cities.append(row[0])

print(len(no_space_cities))



