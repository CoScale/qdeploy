#!/usr/bin/env python
from yaml import load, dump
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from connection import Connection
from logging import Logging
import tasks
import importlib
import datetime
import argparse

parser = argparse.ArgumentParser(description='Start workload.')
parser.add_argument('--test', action='store_true',
                    help="run without executing commands")
args = parser.parse_args()

# Logging
logging = Logging()

# Open yaml file
f = open("deploy.yml", "r")
data = load(f, Loader=Loader)

# Connection
logging.message("# Init connection")
connectionConfig = data['connection']
connection = Connection(config=connectionConfig, logservice=logging, test=args.test)
connection.test()

# Create release name
today = datetime.datetime.today()
release_name = today.strftime('%Y-%m-%d_%H%M%S')
# TODO: Find nicer solution for this
data['deployment']['release_name'] = release_name

# Run tasks one by one
logging.message("# Init tasks")
tasklist = data['tasks']
for taskconfig in tasklist:
    logging.message("! Task %s" % taskconfig['task'])
    TaskClass = getattr(importlib.import_module("tasks"), taskconfig['task'])

    task = TaskClass(connection, {
        "config": taskconfig,
        "deployment": data['deployment']
    }, logging)
    task.run()
