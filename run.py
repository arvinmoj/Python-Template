import argparse
import logging
import sys
from src.main import main

# Set up logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Your Python Project")
    # Add your command-line arguments here
    # parser.add_argument("--option", help="Description of the option")
    args = parser.parse_args()

    try:
        main()
    except Exception as e:
        logging.exception("An error occurred: %s", str(e))
        sys.exit(1)
