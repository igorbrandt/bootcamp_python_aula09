from loguru import logger

# Dependendo do método utilizado com logger, a cor do texto no terminalserá diferente

logger.debug("Aviso para o desenvolvedor, ou eu mesmo, no futuro")
logger.info("Informação importante do processo")
logger.warning("Um aviso ded que algo vai parar de funcionar no futuro")
logger.error("Aconteceeu uma falha")
logger.critical("Aconteceu uma falha que aborta a aplicação")