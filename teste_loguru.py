from loguru import logger

logger.add("logger.log")

def soma(x,y):
    logger.info(x+y)
    return x + y

soma(2,4)