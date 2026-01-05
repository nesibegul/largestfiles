#! /usr/bin/env python3


# now that absolute paths are shown, we can inspect them for file metadata
import os
from os.path import abspath, join, getsize

def largest_files(my_path, n=20):
   
    sizes = {}
    for top_dir, directories, files in os.walk(my_path):
        for _file in files:
            full_path = abspath(join(top_dir, _file))
            #print('this is topdir _ file:', join(top_dir, _file))
            #print('this is full_path', full_path)
            size = getsize(full_path)
            sizes[full_path] = size

    sorted_results = sorted(sizes, key = sizes.get, reverse = True)
    for i in range(10):
        print(50*'*')
    for path in sorted_results[:n]:
        print('Path: {0}, size: {1}'.format(path, sizes[path] ))

if __name__ == '__main__':
    largest_files(r'C:\Users\43117073062\Downloads\INTERVIEW - Kopya', n=10)