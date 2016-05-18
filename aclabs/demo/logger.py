import logging
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

fmt = logging.Formatter(fmt='%(asctime)s: %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(fmt)

logger.addHandler(handler)


def test_logger():
    logger.info("Random info message")
    logger.debug("Random debug message that should not show up"
                 "having INFO log level set")
