
import json
from common.constants import ApiKey
from common.utils import Logger


class TransactionInfo:

  DEFAULT_GAS_PRICE = 21000000 # default gas price, 21 GWei
  DEFUALT_START_GAS = 4700000  # default start gas

  def __init__(self):
    self.nonce = None
    self.gas_price = TransactionInfo.DEFAULT_GAS_PRICE
    self.start_gas = TransactionInfo.DEFUALT_START_GAS
    self.smart_contract_name = None
    self.function_name = None
    self.function_params = []

  @staticmethod
  def fromJson(json_obj):
    obj = TransactionInfo()
    try:
      obj.nonce = json_obj[ApiKey.NONCE]
      obj.gas_price = json_obj.get(ApiKey.GAS_PRICE, TransactionInfo.DEFAULT_GAS_PRICE)
      obj.start_gas = json_obj.get(ApiKey.START_GAS, TransactionInfo.DEFUALT_START_GAS)
      obj.smart_contract_name = json_obj[ApiKey.SMART_CONTRACT_NAME]
      obj.function_name   = json_obj[ApiKey.FUNCTION_NAME]
      obj.function_params = json_obj[ApiKey.FUNCTION_PARAMS]
    except:
      return False, None
    return True, obj

 
