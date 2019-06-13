import sha3


def calc_hash(value):
    return sha3.sha3_256(value.encode("utf-8")).hexdigest()


def alloc_block(prev_hash, data):
    return {"header": {"prev_hash": prev_hash, "data_hash": calc_hash(data)},
            "data": data}


def alloc_hash_chain(genesis_block):
    return {"chain": [genesis_block]}

def calc_block_hash(block):
    header = block["header"]
    return calc_hash(header["prev_hash"]+header["data_hash"])

def make_hash_chain():
    return alloc_hash_chain(alloc_block("0",""))

def append_block(chain, data):
    prev_hash = calc_block_hash(chain["chain"][-1])
    chain["chain"].append(alloc_block(prev_hash, data))
    return chain

def get_length(chain):
    return len(chain["chain"])

def get_block_hash(chain, n):
    return calc_block_hash(chain["chain"][n])

def get_data_hash(chain, n):
    return chain["chain"][n]["header"]["data_hash"]

def get_data(chain,n):
    return chain["chain"][n]["data"]

def verify(chain1, chain2, start, end):
    for n in range(start,end):
        h1 = get_block_hash(chain1,n)
        h2 = get_block_hash(chain2,n)
        print("block{0}-{1} : blockhash(0x{2}...,0x{3}...)".format(n,h1==h2,h1[:8],h2[:8]))

hash_chain1 = make_hash_chain()
append_block(hash_chain1, "total=100;a=100")
append_block(hash_chain1, "total=100;a=80;b=30")
append_block(hash_chain1, "total=100;a=50;b=30;c=20")
print("-"*64)
print(hash_chain1)

hash_chain2 = make_hash_chain()
append_block(hash_chain2, "total=100;a=100")
append_block(hash_chain2, "total=100;a=100")
append_block(hash_chain2, "total=100;a=80;c=20")
print("-"*64)
print(hash_chain2)

print("-"*64)
print(hash_chain1,hash_chain2,1,get_length(hash_chain1))