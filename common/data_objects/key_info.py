
import json
from common.constants import ApiKey


class KeyInfo:
  
  def __init__(self):
    self.alias = None
    self.private_key = None
    self.public_key = None
    self.address = None
  
  def toJson(self):
    return {
      ApiKey.ALIAS       : self.alias,
      ApiKey.PRIVATE_KEY : self.private_key,
      ApiKey.PUBLIC_KEY  : self.public_key,
      ApiKey.ADDRESS     : self.address
    }

  @staticmethod
  def fromJson(json_obj):
    key_info = KeyInfo()
    try:  
      key_info.alias        = json_obj[ApiKey.ALIAS]
      key_info.private_key = json_obj[ApiKey.PRIVATE_KEY]
      key_info.public_key  = json_obj[ApiKey.PUBLIC_KEY]
      key_info.address     = json_obj[ApiKey.ADDRESS]
    except:
      return False, None
    return True, key_info


