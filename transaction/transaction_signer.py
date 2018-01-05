import rlp
import json
import ethereum.abi
from ethereum.transactions import Transaction
from common.constants import TokenType, Constant, SmartContractName
from common.config_manager import ConfigManager
from common.utils import Logger


class TransactionSigner:

  _theta_abi = None

  _theta_token_sale_abi = None

  @staticmethod
  def initialize():
    if not ConfigManager.isInitialized():
      return False
    
    try:
      theta_abi_file_path = ConfigManager.getConfig().getThetaAbiFilePath()
      with open(theta_abi_file_path) as abi_json_data:
        TransactionSigner._theta_abi = json.load(abi_json_data)
    except:
      return False
    if TransactionSigner._theta_abi is None:
      return False
    
    try:
      theta_token_sale_abi_file_path = ConfigManager.getConfig().getThetaTokenSaleAbiFilePath()
      with open(theta_token_sale_abi_file_path) as abi_json_data:
        TransactionSigner._theta_token_sale_abi = json.load(abi_json_data)
    except:
      return False
    if TransactionSigner._theta_token_sale_abi is None:
      return False

    return True
  
  @staticmethod
  def signTransaction(from_addr, nonce, gas_price, start_gas,
    smart_contract_name, function_name, function_params, private_key):
    
    to_addr = TransactionSigner._getToAddress(smart_contract_name)   
    data  = TransactionSigner._getTransactionData(from_addr, smart_contract_name, function_name, function_params)

    if None in [to_addr, data]:
      return False, None

    transaction = Transaction(
        nonce = nonce,
        gasprice = gas_price,
        startgas = start_gas,
        to = to_addr,
        value = 0,
        data = data
    )
    
    transaction.sign(private_key)
    raw_transaction = rlp.encode(transaction)
    hex_transaction = raw_transaction.hex()
    
    return True, hex_transaction

  @staticmethod
  def _getToAddress(smart_contract_name):
    if smart_contract_name == SmartContractName.THETA_TOKEN:
      return ConfigManager.getConfig().getThetaContractAddresss()
    elif smart_contract_name == SmartContractName.THETA_TOKEN_SALE:
      return ConfigManager.getConfig().getThetaTokenSaleContractAddresss()
    else:
      return None

  @staticmethod
  def _getTransactionData(from_addr, smart_contract_name, function_name, function_params):
    if smart_contract_name == SmartContractName.THETA_TOKEN:
      contract_abi = TransactionSigner._theta_abi
    else:
      contract_abi = TransactionSigner._theta_token_sale_abi
    contract = ethereum.abi.ContractTranslator(contract_abi)
    data = contract.encode_function_call(function_name, [function_params])
    #Logger.printInfo("Token transaction data payload: %s"%(data.hex()))
    return data


