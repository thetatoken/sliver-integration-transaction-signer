
import json
from common.data_objects.key_info import KeyInfo
from common.utils import Logger


class KeyInfoManager:

  _key_info_map = {}

  @staticmethod
  def getKeyInfo(key_alias):
    return KeyInfoManager._key_info_map.get(key_alias, None)

  @staticmethod
  def load(path_to_key_info_list_json):
    with open(path_to_key_info_list_json) as key_info_list_json_file:    
      key_info_list_json = json.load(key_info_list_json_file)
    _key_info_map = {}
    for key_info_json in key_info_list_json:
      success, key_info = KeyInfo.fromJson(key_info_json)
      if not success:
        Logger.printError('Failed to parse key info: %s'%(key_info_json))
        return False
      KeyInfoManager._key_info_map[key_info.alias] = key_info
    return True

  
