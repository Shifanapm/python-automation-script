import os
import json
import argparse
from datetime import datetime

CONFIG_FILE = "config.json"
LOG_FILE = "automation_log.txt"

def load_config():
    """Load configuration from JSON file"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        print("Config file not found. Creating a new one...")
        return {}