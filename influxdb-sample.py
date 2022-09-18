from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime
from influxdb import InfluxDB
# client = InfluxDBClient.from_config_file("config.ini")

# write_api = client.write_api(write_options=SYNCHRONOUS)
# query_api = client.query_api()

"""
Prepare data
"""

# _point1 = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
# _point2 = Point("my_measurement").tag("location", "New York").field("temperature", 24.3)
_point3 = Point("my_measurement").tag("location", "Francisco").field("temperature", 19.3)
# write_api.write(bucket="sanghub-bucket", record=[_point1, _point2])
influxDB = InfluxDB("config.ini")
influxDB.write_point("sanghub-bucket",_point3)
"""
Query: using Table structure
"""
# tables = query_api.query(query='''from(bucket:"sanghub-bucket") |> range(start: -10m)''')

# for table in tables:
#     print(table)
#     for record in table.records:
#         print(record.values)

# print()
# print()

"""
Query: using Bind parameters
"""

p = {"_start": datetime.timedelta(hours=-1),
     "_location": "Prague",
     "_desc": True,
     "_floatParam": 25.1,
     "_every": datetime.timedelta(minutes=5)
     }

# tables = query_api.query('''
#     from(bucket:"sanghub-bucket") 
# |> range(start: _start)
#         |> filter(fn: (r) => r["_measurement"] == "my_measurement")
#         |> filter(fn: (r) => r["_field"] == "temperature")
#         |> filter(fn: (r) => r["location"] == _location and r["_value"] > _floatParam)
#         |> aggregateWindow(every: _every, fn: mean, createEmpty: true)
#         |> sort(columns: ["_time"], desc: _desc)
# ''', params=p)
# tables = query_api.query('''
#                     from(bucket: "sanghub-bucket")
#                         |> range(start: _start)
#                         |> filter(fn: (r) => r["_measurement"] == "my_measurement")
#                         |> filter(fn: (r) => r["_field"] == "temperature")
#                         |> filter(fn: (r) => r["location"] == "Prague")
#                     ''', params=p)
# for table in tables:
#     print(table)
#     for record in table.records:
#         print(str(record["_time"]) + " - " + record["location"] + ": " + str(record["_value"]))

print()
print()