import csv

state_list = []

farmers_market = csv.reader(open('farmers-markets-0d51def2d3decd53415dc3b91b0253e8.csv'))
for r in farmers_market:
  if ' ' not in r[4]:
    state_list.append(r[6])
#create list with entry for the state of every row in the farmers market csv where the city did not have a ' ' in the name

west_count = 0
southwest_count = 0
mountain_count = 0
midwest_count = 0
southeast_count = 0
midatlantic_count = 0
northeast_count = 0
noncontiguous_count = 0

for k in state_list:
  if k == 'Washington' or k == 'Oregon' or k == 'California':
    west_count += 1
  if k == 'Arizona' or k == 'New Mexico' or k == 'Texas' or k == 'Oklahoma':
    southwest_count += 1
  if k == 'Idaho' or k == 'Nevada' or k == 'Montana' or k == 'Utah' or k == 'Colorado' or k == 'Wyoming':
    mountain_count += 1
  if k == 'North Dakota' or k == 'South Dakota' or k == 'Nebraska' or k == 'Kansas' or k == 'Minnesota' or k == 'Iowa' or k == 'Missouri' or k == 'Wisconsin' or k == 'Illinois' or k == 'Indiana' or k == 'Michigan' or k == 'Ohio':
    midwest_count += 1
  if k == 'Arkansas' or k == 'Louisiana' or k == 'Kentucky' or k == 'Tennessee' or k == 'Mississippi' or k == 'Alabama' or k == 'Georgia' or k == 'Florida' or k == 'North Carolina' or k == 'South Carolina':
    southeast_count += 1
  if k == 'Virginia' or k == 'West Virginia' or k == 'Maryland' or k == 'Delaware' or k == 'New Jersey' or k == 'Pennsylvania':
    midatlantic_count += 1
  if k == 'New York' or k == 'Massachusetts' or k == 'Rhode Island' or k == 'Connecticut' or k == 'New Hampshire' or k == 'Vermont' or k == 'Maine':
    northeast_count += 1
  if k == 'Alaska' or k == 'Hawaii':
    noncontiguous_count += 1

print 'West coast region: %d' % (west_count)
print 'Southwest region: %d' % (southwest_count)
print 'Mountain region: %d' % (mountain_count)
print 'Midwest region: %d' % (midwest_count)
print 'Southeast region: %d' % (southeast_count)
print 'Mid-Atlantic region: %d' % (midatlantic_count)
print 'Northeast region: %d' % (northeast_count)
print 'Noncontiguous region: %d' % (noncontiguous_count)

