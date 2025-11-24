import logging
import sys

def setup_logging():
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logging.root.setLevel(logging.INFO)
    logging.root.addHandler(handler)
