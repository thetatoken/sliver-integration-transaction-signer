
class TokenType:
  ETHER = 'ETHER'
  THETA = 'THETA'


class Constant:
  pass


class ApiStatus:
  OK      = 'OK'
  SUCCESS = 'SUCCESS'
  ERROR   = 'ERROR'


class ApiKey:
  STATUS       = 'status'
  ERROR_CODE   = 'error_code'
  MESSAGE      = 'message'
  BODY         = 'body'

  USER_ID = 'user_id'
  FROM    = 'from'
  TO      = 'to'
  NONCE   = 'nonce'
  GAS_PRICE = 'gas_price'
  START_GAS = 'start_gas'
  VALUE   = 'value'
  TOKEN_TYPE = 'token_type'
  SIGNED_TX = 'signed_transaction'
  
  ALIAS       = 'alias'
  PRIVATE_KEY = 'private_key'
  PUBLIC_KEY  = 'public_key'
  ADDRESS     = 'address'
  ADDRESSES   = 'addresses'

  NONCE     = 'nonce'
  GAS_PRICE = 'gas_price'
  START_GAS = 'start_gas'
  FUNCTION_NAME   = 'function_name'
  FUNCTION_PARAMS = 'function_params'
  EXCHANGE_RATE   = 'exchange_rate'

  RAW_TRANSACTION = 'raw_transaction'
  SMART_CONTRACT_NAME = 'smart_contract_name'



class ApiErrorCode:
  NO_ERROR  = 0

  # Generic errors
  GENERIC_ERROR           = 10000
  SERVER_CONNECTION_ERROR = 10001
  INVALID_RESPONSE_FORMAT = 10002
  QUERY_PARAM_MISSING     = 10003

  # Address generation
  ADDR_FAILURE = 20001 

  # Transaction signing
  TX_SIGNING_FAILURE = 30001
  FUNCTION_NOT_SUPPORTED = 30002


class SmartContractName:
  THETA_TOKEN = 'theta_token'
  THETA_TOKEN_SALE = 'theta_token_sale'


class SupportedFunctionName:
  ADD_ACCOUNTS_TO_WHITELIST = 'addAccountsToWhitelist'
  SET_EXCHANGE_RATE = 'setExchangeRate'


class KeyAlias:
  WHITELIST_CONTROLLER = 'whitelist_controller'
  EXCHANGE_RATE_CONTROLLER = 'exchange_rate_controller'



