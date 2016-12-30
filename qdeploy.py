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

# Logging
logging = Logging()

# Open yaml file
f = open("deploy.yml", "r")
data = load(f, Loader=Loader)

# Connection
logging.message("# Init connection")
connectionConfig = data['connection']
connection = Connection(connectionConfig, logging)
connection.test()


logging.message("# Init tasks")
# Run tasks one by one
tasklist = data['tasks']
for taskconfig in tasklist:
    logging.message("! Task %s: %s" % (taskconfig['task'], taskconfig['name']))
    TaskClass = getattr(importlib.import_module("tasks"), taskconfig['task'])
    task = TaskClass(connection, taskconfig, logging)
    task.run()
