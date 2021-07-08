#see https://web3py.readthedocs.io/en/stable/ens_overview.html
from web3 import Web3
from ens import ENS

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/{your_token}', request_kwargs={'timeout': 60}))
ns = ENS.fromWeb3(w3)
ens = ns.name('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045')
print(ens)
