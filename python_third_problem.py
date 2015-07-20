import csv
farmers_market = open('farmers-markets-0d51def2d3decd53415dc3b91b0253e8.csv')
csv_farmers_market = csv.reader(farmers_market)

total_count = 0

for row in csv_farmers_market:
  if (row[6] == 'Minnesota' or row[6] == 'Iowa' or row[6] == 'Missouri' or row[6] == 'Arkansas' or row[6] == 'Louisiana' or row[6] == 'North Dakota' or row[6] == 'South Dakota' or row[6] == 'Nebraska' or row[6] == 'Kansas' or row[6] == 'Oklahoma' or row[6] == 'Texas') and ' ' not in row[4]:
    total_count += 1
  elif ' ' not in row[4] and (row[6] == 'Colorado' or row[6] == 'New Mexico') and row[16] >= -106.445:
    total_count += 1
  elif ' ' not in row[4] and (row[6] == 'Montana' or row[6] == 'Wyoming') and row[16] >= -110.971:
    total_count += 1

print total_count



