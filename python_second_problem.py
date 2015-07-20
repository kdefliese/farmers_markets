import csv
from collections import Counter

farmers_market = csv.DictReader(open('farmers-markets-0d51def2d3decd53415dc3b91b0253e8.csv'))
state_populations = csv.DictReader(open('state_populations.csv'))

state_list = []
state_list_2 = []

for r in state_populations:
  state_list.append(r['state_name'])
# made list of the states

for r in farmers_market:
  if ' ' not in r['city']:
    for x in range(0, 51):
      if r['State'] in state_list[x]:
        state_list_2.append(r['State'])
# made list containing an entry for each time a state appears in the farmers_market csv file

my_dict = dict(Counter(state_list_2))
# made dictionary of states: farmers markets counts
print my_dict

state_populations = csv.reader(open('state_populations.csv'))
d = dict(state_populations)
del d['state_name']
# made dictionary of states: populations and removed the extra entry created by the header in the csv file
print d

new_dict = {}
for key in my_dict:
  result = my_dict[key] / float(d[key])
  result = '{:.10f}'.format(result)
  new_dict[key] = result

# calculated farmers markets per capita for each state

maximum = max(new_dict.values())
minimum = min(new_dict.values())
# calculate max and min states per capita

for key in new_dict:
  if new_dict[key] == maximum:
    print 'The max is %s' % (key)
  elif new_dict[key] == minimum:
    print 'The min is %s' % (key)
# print max and min states per capita



