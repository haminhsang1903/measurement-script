from time import sleep
import psutil
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from influxdb import InfluxDB
# print(psutil.virtual_memory())
# print(psutil.cpu_percent(1))

for proc in psutil.process_iter():
    if proc.name() == "Zalo":
        print(proc.pid)
        print(proc.num_threads())
        print(proc.cpu_percent(1))
        print(proc.memory_percent())
# count = 0;
# influxDB = InfluxDB("config.ini")
# while True:
#     count += 1;
#     _point3 = Point("my_measurement").tag("cpu", "cpu_percent").field("temperature", psutil.cpu_percent(1)).time(time=datetime.utcnow())
#     # write_api.write(bucket="sanghub-bucket", record=[_point1, _point2])
#     influxDB.write_point("sanghub-bucket",_point3)
#     _point4 = Point("my_measurement").tag("mem", "mem_percent").field("temperature", psutil.virtual_memory().percent).time(time=datetime.utcnow())
#     # write_api.write(bucket="sanghub-bucket", record=[_point1, _point2])
#     influxDB.write_point("sanghub-bucket",_point4)
#     if count == 100:
#         break;
#     sleep(1)