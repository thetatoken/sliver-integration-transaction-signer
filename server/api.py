import os
import json
from common.utils import Logger
from common.constants import ApiKey, ApiErrorCode, KeyAlias
from common.constants import SupportedFunctionName, SmartContractName
from common.http.response import HttpSuccess, HttpError
from transaction.key_info_manager import KeyInfoManager
from transaction.transaction_signer import TransactionSigner
from flask_restful import request, reqparse, abort, Api, Resource


class WhitelistResource(Resource):

  def get(self):
    addresses = request.args.getlist(ApiKey.ADDRESS, None)
    nonce     = request.args.get(ApiKey.NONCE, None)
    gas_price = request.args.get(ApiKey.GAS_PRICE, None)
    start_gas = request.args.get(ApiKey.START_GAS, None)
    if None in [addresses, nonce, gas_price, start_gas]:
      return HttpError(
        error_code = ApiErrorCode.QUERY_PARAM_MISSING,
        message = 'Query parameter missing! requires address, nonce, gas_price, and start_gas!').toJson()
    
    nonce = int(nonce)
    gas_price = int(gas_price)
    start_gas = int(start_gas)
    function_name = SupportedFunctionName.ADD_ACCOUNTS_TO_WHITELIST
    function_params = addresses
    key_info = KeyInfoManager.getKeyInfo(KeyAlias.WHITELIST_CONTROLLER)

    success, signed_tx = TransactionSigner.signTransaction(
      from_addr = key_info.address,
      nonce = nonce,
      gas_price = gas_price,
      start_gas = start_gas,
      smart_contract_name = SmartContractName.THETA_TOKEN_SALE,
      function_name = function_name,
      function_params = function_params,
      private_key = key_info.private_key)
    
    if not success:
      return HttpError(
        error_code = ApiErrorCode.TX_SIGNING_FAILURE,
        message = 'Failed to sign the transaction!').toJson()
    
    Logger.printInfo('Signed transaction - nonce: %s, function_name: %s, function_params: %s, signed_tx: %s'%\
      (nonce, function_name, function_params, signed_tx))
   
    return HttpSuccess({ApiKey.SIGNED_TX : signed_tx}).toJson()


