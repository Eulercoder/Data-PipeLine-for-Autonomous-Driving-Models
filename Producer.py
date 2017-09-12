from kafka import KafkaProducer
from kafka.errors import KafkaError
# import logging
import json, csv, glob

def rowToString(row):
	s = ""
	for i in row:
		s = s + i + " "
	return s[:len(s)-1]

# logging.basicConfig(level = logging.DEBUG)
producer = KafkaProducer(bootstrap_servers='localhost:9092')
file_dirs = glob.glob('./Data/*.csv')
for file in file_dirs:
	with open(file, "r") as f_obj:
		reader = csv.DictReader(f_obj)
		# Skip the first line
		count = False
		for row in reader:
			if count is not True:
				count = True
				continue
			
			producer.send('my-topic', json.dumps(row).encode())

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)