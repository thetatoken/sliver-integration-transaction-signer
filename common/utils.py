
import re
import sys
import subprocess
import time
import calendar
import threading
from datetime import datetime


#def toUnicode(item):
#  if isinstance(item, str):
#    item_unicode = unicode(item, errors='ignore')
#  else:
#    item_unicode = unicode(item)
#  return item_unicode

def toUnicode(item):
  return str(item)


class TimeUtils:

  @staticmethod
  def utcSecondsSinceEpoch():
    seconds = int(round(calendar.timegm(time.gmtime())))
    return seconds
  
  @staticmethod
  def utcMillisecondsSinceEpoch():
    milliseconds = int(round(1000 * calendar.timegm(time.gmtime())))
    return milliseconds


class Logger(object):

  DEBUG_MODE = False
  LOG_FILE_PATH = None

  @staticmethod
  def enableDebugLog(enabled = True):
    Logger.DEBUG_MODE = enabled

  @staticmethod
  def setLogFolder(log_file_folder):
    Logger.LOG_FILE_PATH = log_file_folder + '/log_' + str(TimeUtils.utcSecondsSinceEpoch()) + '.txt'

  @staticmethod
  def printInfo(msg):
    printed_msg = str(datetime.now()) + '\033[97m [Info, %s] %s \033[0m'%(Logger._getThreadName(), toUnicode(msg))
    Logger._writeToLogFile(printed_msg)
    print(printed_msg)
    sys.stdout.flush()
    return printed_msg

  @staticmethod
  def printWarning(msg):
    printed_msg = str(datetime.now()) + '\033[93m [Warning, %s] %s \033[0m'%(Logger._getThreadName(), toUnicode(msg))
    Logger._writeToLogFile(printed_msg)
    print(printed_msg)
    sys.stdout.flush()
    return printed_msg

  @staticmethod
  def printError(msg):
    printed_msg = str(datetime.now()) + '\033[91m [Error, %s] %s \033[0m'%(Logger._getThreadName(), toUnicode(msg))
    Logger._writeToLogFile(printed_msg)
    print(printed_msg)
    sys.stdout.flush()
    return printed_msg

  @staticmethod
  def printDebug(msg):
    printed_msg = str(datetime.now()) + '\033[50m [Debug, %s] %s \033[0m'%(Logger._getThreadName(), toUnicode(msg))
    Logger._writeToLogFile(printed_msg)
    if Logger.DEBUG_MODE:
      print(printed_msg)
      sys.stdout.flush()
    return printed_msg

  @staticmethod
  def _writeToLogFile(msg):
    if Logger.LOG_FILE_PATH is not None:
      log_file = open(Logger.LOG_FILE_PATH, 'w') 
      log_file.write(msg + '\n')
      log_file.close()

  @staticmethod
  def _getThreadName():
    thread_name = threading.currentThread().getName()
    return thread_name


class ErrorReporter:

  @staticmethod
  def reportError(error_message):
    printed_error_msg = Logger.printError(error_message)
    # TODO: send out email...


