import csv
import os
import time
from dataclasses import fields, asdict
import logging

logger = logging.getLogger(__name__)

class DataPipeline:
    def __init__(self, csv_filename='', storage_queue_limit=50):
        self.names_seen = []
        self.storage_queue = []
        self.storage_queue_limit = storage_queue_limit
        self.csv_filename = csv_filename
        self.csv_file_open = False

    
    def save_to_csv(self):
        self.csv_file_open = True
        data_to_save = self.storage_queue[:]
        self.storage_queue.clear()
        if not data_to_save:
            return
        keys = [field.name for field in fields ( data_to_save[0])]
        file_exists = os.path.isfile(self.csv_filename) and os.path.getsize(self.csv_filename) >0
        with open(self.csv_filename, mode='a', newline='',encoding='utf-8') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=keys)
            if not file_exists:
                writer.writeheader()
            for item in data_to_save: 
                writer.writerow(asdict(item))
        self.csv_file_open = False
    
    def add_data(self, scraped_data):
        if not self.is_duplicate(scraped_data):
            self.storage_queue.append(scraped_data)
            if len (self.storage_queue) >= self.storage_queue_limit and not self.csv_file_open:
                self.save_to_csv()
    
    def is_duplicate ( self, input_data):
        if input_data.name in self.names_seen: 
            logger.warning(f"Duplicate item found: {input_data.name}")
            return True
        self.names_seen.append(input_data.name)
        return False
    
    def close_pipeline (self):
        if self.csv_file_open:
            time.sleep(5)
        if len (self.storage_queue)> 0:
            self.save_to_csv()
            
    
