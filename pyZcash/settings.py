import os, re
#ZCASH RPC
# Address and port of local zcashd testnet rpc
ZURL = "http://localhost:18232"
#Timeout needs to be high for any pour operations
TIMEOUT = 600
#Default fee to use on network for txs.
DEFAULT_FEE = 0.01

zcashconf = os.path.expanduser('~/.zcash/zcash.conf')

def read_config(filename):
    f = open(filename)
    for line in f:
        if re.match('rpcuser', line):
            user = line.strip('\n').split('=')[1]
        if re.match('rpcpassword', line):
            password = line.strip('\n').split('=')[1]
    return (user, password)

config = read_config(zcashconf)
# from zcash conf
RPCUSER = config[0]
RPCPASSWORD = config[1]

#TESTS
#for tests (sample data here - replace with your own)
TEST_TXID = ''
TEST_ZADDR = ""
TEST_TADDR = ""
TEST_ZSECRET = ""
