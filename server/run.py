import sys; sys.path.append('../')
import os
import logging
from flask import Flask
from flask import request
from flask_restful import Api
from common.constants import KeyAlias
from common.utils import Logger
from common.config_manager import ConfigManager
from transaction.key_info_manager import KeyInfoManager
from transaction.transaction_signer import TransactionSigner
from api import WhitelistResource
from api import ExchangeRateResource


def initialize(path_to_config_file, path_to_key_info_json):
  log = logging.getLogger('werkzeug')
  log.setLevel(logging.ERROR)
  success = ConfigManager.load(path_to_config_file)
  if not success:
    return False

  config = ConfigManager.getConfig()
  Logger.setLogFolder(config.server_log_file_folder)
  success = TransactionSigner.initialize()
  if not success:
    return False

  success =  KeyInfoManager.load(path_to_key_info_json)
  if not success:
    return False

  if KeyInfoManager.getKeyInfo(KeyAlias.WHITELIST_CONTROLLER) == None:
    Logger.printError('%s key info not loaded!'%(KeyAlias.WHITELIST_CONTROLLER))
    return False

  if KeyInfoManager.getKeyInfo(KeyAlias.EXCHANGE_RATE_CONTROLLER) == None:
    Logger.printError('%s key info not loaded!'%(KeyAlias.EXCHANGE_RATE_CONTROLLER))
    return False

  success = TransactionSigner.initialize()
  if not success:
    return False

  return True


app = Flask(__name__)
api = Api(app)
api.add_resource(WhitelistResource,    '/whitelist/sign')
api.add_resource(ExchangeRateResource, '/exchange_rate/sign')


if __name__ == '__main__':
  path_to_config_file = '../config.json'
  path_to_key_info_json = '../data/key_info.json'
  success = initialize(path_to_config_file, path_to_key_info_json)
  if not success:
    exit(1)

  host = '0.0.0.0'
  port = ConfigManager.getConfig().getPort()
  Logger.printInfo('Running test server at %s:%s'%(host, port))
  app.run(threaded=True, debug=True, host=host, port=port)


