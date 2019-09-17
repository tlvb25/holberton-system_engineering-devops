#!/usr/bin/env bash
from sys import argv
import requests

if __name__ == "__main__":
    output = fetch('https://jsonplaceholder.typicode.com/users/argv[1]/todos')
    .then(response => response.json())
    .then(json => console.log(json))
