import logging
import os
import configparser

config= configparser.ConfigParser()
config.read('config.ini')

if not os.path.exists("logs"):
    os.makedirs("logs", exist_ok=False)

logging.basicConfig(
    filename=config.get('settings', 'CONFIG_PATH'),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_example():
    
    logging.info("Pipeline started successfully.")
    try:
        # simulate some operation
        10 / 0
    except Exception as e:
        logging.error(f"Error occurred: {e}")

log_example()