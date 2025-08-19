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

def save_config(config):
    """Save updated configuration back to file"""
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def log_changes(config):
    """Log updates to a text file"""
    with open(LOG_FILE, "a") as log:
        log.write(f"Updated on {config['last_updated']} | Version: {config['version']} | Project: {config.get('project_name')} | Author: {config.get('author')}\n")

def main():
    parser = argparse.ArgumentParser(description="Automation Script for Config Updates")
    parser.add_argument("--project", help="Set project name")
    parser.add_argument("--author", help="Set author name")
    parser.add_argument("--version", help="Set version manually")

    args = parser.parse_args()

    config = load_config()
    updated_config = update_config(config, args.project, args.author, args.version)
    save_config(updated_config)
    log_changes(updated_config)

    print("✅ Configuration updated successfully!")
    print("📌 Current Config:", updated_config)

if __name__ == "__main__":
    main()