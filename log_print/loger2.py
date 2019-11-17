import  logging
import  logging.handlers
import datetime
import os,sys
#import win32evtlogutil, win32evtlog

logger = logging.getLogger('xyhlogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s) - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#dllname_f=os.path.join(r"D:\python\Lib\site-packages\win32\win32service.pyd")
ntl_handler = logging.handlers.NTEventLogHandler("python Test logging")
ntl_handler.setLevel(logging.INFO)

syslog_handler = logging.handlers.SysLogHandler("syslog xuyh")
syslog_handler.setLevel(logging.ERROR)

logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.addHandler(ntl_handler)
logger.addHandler(syslog_handler)

# logger.debug('debug msg')
# logger.info('info msg')
# logger.warning('warning msg')
# logger.error('error msg')
logger.critical('critical msg')