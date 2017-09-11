from kafka import KafkaProducer
from kafka.errors import KafkaError
# import logging
import csv, glob

def rowToString(row):
	s = ""
	for i in row:
		s += i
		s += " "
	# print(s)
	return s[:len(s)-1]

# logging.basicConfig(level = logging.DEBUG)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

file_dirs = glob.glob('./Data/*.csv')
for file in file_dirs:
	csv_path = file
	# csv_path = "_slash_vehicle_slash_tire_pressure_report.csv"
	with open(csv_path, "r") as f_obj:
		reader = csv.reader(f_obj)
		count = False
		for row in reader:
			if count is not True:
				count = True
				continue
			producer.send('my-topic', key = str.encode(csv_path[7:]), value = str.encode(rowToString(row)))

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)