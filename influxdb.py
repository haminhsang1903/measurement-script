from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime

class InfluxDB():
    def __init__(self, config_path):
        self.client = InfluxDBClient.from_config_file(config_path)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()
        
    def write_point(self, bucket_name, list_points):
        self.write_api.write(bucket=bucket_name, record=list_points)
        
    # def query_tables(self, input_query, param):
    #     tables = self.query_api.query(query= input_query, params=param)
    #     for table in tables:
    #         for record in table.records:
                