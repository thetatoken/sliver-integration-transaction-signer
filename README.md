# theta-token-sale-transaction-signer

## Ubuntu dependencies

### Tools and Libraries

```
python3, python3-pip, libssl-dev
```

### Python models

```
pysha3, ecdsa, psycopg2
flask, sqlalchemy, guess_language, flipflop, requests
schedule, boto, filechunkio
pyethereum
```

## Run the service

```
cd theta-token-sale-transaction-signer/server
python3 run.py

```

### Example config.json

```
# Place under theta-token-sale-transaction-signer

{
  "port" : 6027,
  "server_log_file_folder" : "<path/to/log/file>",
  "theta_contract_address" : "<theta_token_contract_address>",
  "theta_abi_file_path" : "../data/ThetaToken.json",
  "theta_token_sale_contract_address" : "<theta_token_sale_contract_address>",
  "theta_token_sale_abi_file_path" : "../data/ThetaTokenSale.json"
}

```

