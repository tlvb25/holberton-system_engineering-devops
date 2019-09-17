#!/usr/bin/env bash
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
print (r)
