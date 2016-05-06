import json, redis, time

neighborhoods = []
crushes = []

file = open('ResultsRedis.geojson', 'w')

r = redis.StrictRedis(host='localhost', port='6379', db=0)
r.flushall()

startdata = time.time()
print(startdata)
with open('Neighborhoods.geojson', encoding='utf-8') as data_file:
    test_data = json.load(data_file)

for i in test_data['features']:
    neighborhoods.append(i['properties']['NAME'])

    #print(names, polygon)
for row in test_data['features']:
   for i in row['geometry']['coordinates'][0]:
       r.hset(row['properties']['NAME'], i[0], i[1])
   #print(r.hgetall(row['properties']['NAME']))


with open('crushes.geojson', encoding='utf-8') as data_file1:
       test_data1 = json.load(data_file1)
for row2 in test_data1['features']:
    crushes.append(row2['properties']['OBJECTID'])
    r.hset(row2['properties']['OBJECTID'], row2['geometry']['coordinates'][0], row2['geometry']['coordinates'][1])

enddata = time.time() - startdata
print(enddata)

count = 0
startjoin = time.time()
print(startjoin)
for i in neighborhoods:
    for j in crushes:
        if (min(r.hkeys(i)) <= min(r.hkeys(j)) <= max(r.hkeys(i))):
            if (min(r.hvals(i)) <= min(r.hvals(j)) <= max(r.hvals(i))):
                r.hset('results', r.hkeys(j), r.hvals(j))
                count = count + 1
                #print(count)


endjoin = time.time() - startjoin
print(endjoin)
print(count)
data_file.close()
data_file1.close()