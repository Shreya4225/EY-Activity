import logging

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

logging.debug("this is debug message")
logging.info("Application started")
logging.warning("Log memory warning")
logging.error("File not found error")
logging.critical("Critical system failure")