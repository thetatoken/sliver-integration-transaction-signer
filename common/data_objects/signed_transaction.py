

class SignedTransaction:

  def __init__(self, nonce, raw_transaction):
    self.nonce = nonce
    self.raw_transaction = raw_transaction

  def toJson(self):
    return {
      ApiKey.NONCE : self.nonce,
      ApiKey.RAW_TRANSACTION : self.raw_transaction
    }


