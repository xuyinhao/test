# 日志发生的事件，位置，严重级别，内容
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s -[%(users)s:%(ip)s] - %(message)s"
DATA_FORMAT= "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig( level=logging.DEBUG, format=LOG_FORMAT,
                    datefmt=DATA_FORMAT)
# logging.debug('%s debug %d',"tom",10)
logging.info("this is info log.",exc_info=False ,stack_info=False ,extra={'users':'Tom','ip':'13.13.13.13'})
# logging.warning('warning')
# logging.error("error")
# logging.critical("critical")