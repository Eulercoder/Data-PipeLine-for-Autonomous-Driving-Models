import csv
import json

csvfile = open('_slash_vehicle_slash_tire_pressure_report.csv', 'r')
jsonfile = open('file.json', 'w')

# fieldnames = ("rosbagTimestamp","header","seq","stamp", "secs", "nsecs", "frame_id", "front_left", "front_right", "rear_left", "rear_right")
# reader = csv.DictReader(csvfile, fieldnames)
# count = False
# for row in reader:
#     if count is not True:
#     	count = True
#     	continue
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')

reader = csv.DictReader(csvfile)
count = False
for row in reader:
    if count is not True:
    	count = True
    	continue
    print(row)
    # json.dump(row, jsonfile)
    # jsonfile.write('\n')
    # print(row)