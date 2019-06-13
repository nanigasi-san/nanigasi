import sha3

def calc_hash(value):
    return sha3.sha3_256(value.encode("utf-8")).hexdigest()

m1 = "{a:100, b:200}"
m2 = "{a:100, b:200}"

h1 = calc_hash(m1)
h2 = calc_hash(m2)
print("m1: {0},hash: 0x{1}".format(m1,h1))
print("m2: {0},hash: 0x{1}".format(m2,h2))

m3 = "{a:101, b:200}"
h3 = calc_hash(m3)
print("m3: {0},hash: 0x{1}".format(m3,h3))

"""
m1: {a:100, b:200},hash: 0xac71e6ae0aff36a1ce14520f22278a10e73c75456b60a092e236f39dd461b6a9
m2: {a:100, b:200},hash: 0xac71e6ae0aff36a1ce14520f22278a10e73c75456b60a092e236f39dd461b6a9
m3: {a:101, b:200},hash: 0x4212091dff9cebbe3c83d5acabde6946f7e5d0bc40bfbb48edb167eec1c862df
"""