#!/usr/bin/env python3
import logging
import os
import schedule
import sys
import time

LOGGER = logging.getLogger('app')
LOGGER_FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT)


def do_something():
    LOGGER.info("[SCHEDULER] doing something...")


def main():
    LOGGER.info(f"Welcome to my app")
    schedule.every(3).seconds.do(do_something)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            LOGGER.info("Exiting by user request.")
            sys.exit(0)
        except Exception:  # catch *all* exceptions
            LOGGER.error("Fatal error in main loop", exc_info=True)
            sys.exit(1)


if __name__ == "__main__":
    main()
