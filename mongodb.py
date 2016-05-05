import pymongo
import json, time, sys

m = pymongo.MongoClient('localhost', 27017)
db = m.test
file = open('resultintersect.geojson', 'w')
file2 = open('resultwithin.geojson', 'w')


neighborhoods = []
crushes = []
crushes.append([])
crushes.append([])
neighborhoods.append([])
neighborhoods.append([])

startdata = time.time()
print(startdata)
f1 = open('Neighborhoods.geojson', encoding='utf-8')
test_data = json.load(f1)

for row in test_data['features']:
       neighborhoods[0].append(row['properties']['NAME'])
       neighborhoods[1].append(row['geometry']['coordinates'])
       db.neighborhoods.insert(
           {'name':row['properties']['NAME'], 'type': 'Polygon', 'coordinates': row['geometry']['coordinates'][0]})

f2 = open('crushes.geojson', encoding='utf-8')
test_data1 = json.load(f2)
for row2 in test_data1['features']:
   crushes[0].append(row2['properties']['OBJECTID'])
   crushes[1].append(row2['geometry']['coordinates'])
   db.crushes.insert(
       {'name': row2['properties']['OBJECTID'], 'type': 'Point',
        'coordinates': row2['geometry']['coordinates']})

enddata = time.time() - startdata
print('/n', enddata)

count = 0
startintersect = time.time()
print(startintersect)

for n in neighborhoods[1]:
    for d1 in db.crushes.find({'coordinates':
                     {'$geoIntersects':
                      {'$geometry':{'type': 'Polygon',
                                     'coordinates': n}
                       }}}):
         #file.write(d1)
            count = count + 1
            #print(count, d1)

endintersect = time.time() - startintersect
print(endintersect)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

countWithin = 0
startWithin = time.time()
print(startWithin)
for n in neighborhoods[1]:
    for d1 in db.crushes.find({'coordinates':
                     {'$geoWithin':
                      {'$geometry':{'type': 'Polygon',
                                     'coordinates': n}
                       }}}):
         #file2.write(d1)
            countWithin = countWithin + 1
            #print(countWithin, d1)

endWithin = time.time() - startWithin
print(endWithin)