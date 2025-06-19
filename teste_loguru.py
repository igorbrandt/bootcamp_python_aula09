from loguru import logger

logger.add("logger.log")

def soma(x,y):
    try:
        soma = x + y
        logger.info("Valores corretos")
        return soma
    except:
        logger.critical("Valores incorretos")

soma(2,"sds")