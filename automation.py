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
    
def update_config(config, project_name=None, author=None, version=None):
    """Update configuration values"""
    config["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if project_name:
        config["project_name"] = project_name
    if author:
        config["author"] = author
    if version:
        config["version"] = version
    else:
        # If version not provided, auto increment
        config["version"] = str(float(config.get("version", "1.0")) + 0.1)
    
    return config