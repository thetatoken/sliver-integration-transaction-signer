import json
from common.utils import Logger
import traceback


class ConfigKey:
  PORT = 'port'
  SERVER_LOG_FILE_FOLDER = 'server_log_file_folder'
  THETA_CONTRACT_ADDRESS = 'theta_contract_address'
  THETA_ABI_FILE_PATH    = 'theta_abi_file_path'
  THETA_TOKEN_SALE_CONTRACT_ADDRESS = 'theta_token_sale_contract_address'
  THETA_TOKEN_SALE_ABI_FILE_PATH = 'theta_token_sale_abi_file_path'


class Config:

  def __init__(self):
    self.port = None
    self.server_log_file_folder = None
    self.theta_contract_address = None
    self.theta_abi_file_path    = None
    self.theta_token_sale_contract_address = None
    self.theta_token_sale_abi_file_path = None

  def getDBUri(self):
    return 'sqlite:///./test.db'

  def getPort(self):
    return self.port

  def getServerLogFileFolder(self):
    return self.server_log_file_folder

  def getThetaContractAddresss(self):
    return self.theta_contract_address

  def getThetaAbiFilePath(self):
    return self.theta_abi_file_path

  def getThetaTokenSaleContractAddresss(self):
    return self.theta_token_sale_contract_address

  def getThetaTokenSaleAbiFilePath(self):
    return self.theta_token_sale_abi_file_path


class ConfigManager:

  _config = Config()

  _initialized = False
   
  @staticmethod
  def load(path_to_config_json):
    with open(path_to_config_json) as config_json_file:    
      config_json = json.load(config_json_file)
   
    config = ConfigManager._config
    try:
      config.port = config_json[ConfigKey.PORT]
      config.server_log_file_folder = config_json[ConfigKey.SERVER_LOG_FILE_FOLDER]
      config.theta_contract_address = config_json[ConfigKey.THETA_CONTRACT_ADDRESS]
      config.theta_abi_file_path    = config_json[ConfigKey.THETA_ABI_FILE_PATH]
      config.theta_token_sale_contract_address = config_json[ConfigKey.THETA_TOKEN_SALE_CONTRACT_ADDRESS]
      config.theta_token_sale_abi_file_path = config_json[ConfigKey.THETA_TOKEN_SALE_ABI_FILE_PATH]
    except:
      Logger.printError('Failed to load config file! file path: %s %s'%(path_to_config_json, traceback.print_exc()))
      return False

    ConfigManager._initialized = True
    return True

  @staticmethod
  def isInitialized():
    return ConfigManager._initialized
    
  @staticmethod
  def getConfig():
    return ConfigManager._config


