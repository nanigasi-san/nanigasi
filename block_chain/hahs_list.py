import sha3

def calc_hash(value):
    return sha3.sha3_256(value.encode("utf-8")).hexdigest()

def alloc_hash_list(root, lst, chunks):
    return {"root_hash": root, "hash_list": lst, "chunks": chunks}

def calc_root_hash(hash_list):
    return calc_hash("".join(hash_list))

def chunk(data, size):
    return [data[i:i+size] for i in range(0,len(data),size)]

def make_hash_list(data, chunk_size):
    chunks = chunk(data,chunk_size)
    lst = [calc_hash(c) for c in chunks]
    return alloc_hash_list(calc_root_hash(lst), lst, chunks)

def get_root_hash(lst):
    return lst["root_hash"]

def get_hash_list(lst):
    return lst["hash_list"]

def get_data_chunk(lst, n):
    return lst["chunks"][n]

def get_data(lst):
    return "".join(lst["chunks"])

message1 = "aaabbbcccdddeee"
hash_list1 = make_hash_list(message1,3)
print("-"*64)
print(hash_list1)
print(get_data(hash_list1))

message2 = "aaabbbcccdddeez"
hash_list2 = make_hash_list(message2,3)
print("-"*64)
print(hash_list2)
print(get_data(hash_list2))

trusted_root_hash = get_root_hash(hash_list1)
untrusted_hash_list = get_hash_list(hash_list2)
untrusted_root_hash = calc_root_hash(untrusted_hash_list)
print("-"*64)
print("{0}-trusted: 0x{1}..., untrusted: 0x{2}...".format(trusted_root_hash==untrusted_root_hash,trusted_root_hash[:8],untrusted_root_hash[:8]))