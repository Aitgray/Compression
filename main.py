# I'll be using PyQt for the GUI and gzip for the compression
# I'll be using the PyQt5 library
# I'll be using the shutil library to copy the file objects

# I also need to figure out how multi-threading works in python
# Additionally I'm going to need to implement error handling

# I also want to add a categorization feature to the app, so that the user can categorize the files they compress
# This categorization could also be partially automated, by having the app look at the file extension and categorize it based on that
# for photos specifically, I can use openCV to look at the photo and categorize it based on the contents of the photo

# I'll use a dynamically scaling hashmap for my categorization system

from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
import gzip
import pathlib
import os
import cv2

class HashTable():
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_val
        else:
            return "N/A"
        
    def delete_val(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        return

    


class CompressionApp():
    def __init__(self):
        super().__init__()

        #ui setup will go here
        # we need some sort of file selection button as well as a button to compress or decompress
        # we also need a text box to display the status of the compression/decompression


    def compress_file(self, filename):
        with open(filename, 'rb') as f_in:
            with gzip.open(filename + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def decompress_file(self, filename):
        with gzip.open(filename, 'rb') as f_in:
            with open(filename[:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def select_files(self):
        # use a file dialog to select files and call self.compress_file or self.decompress_file
        pass

#to run the app:
app = QtWidgets.QApplication([])
window = CompressionApp()
window.show()
app.exec_()