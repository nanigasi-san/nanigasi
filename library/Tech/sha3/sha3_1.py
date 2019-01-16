import sha3
def calc_hash(value):
    return sha3.sha3_256(value.encode("utf-8")).hexdigest()
m1 = "{ a: 100, b: 200 }"
m2 = "{ a: 100, b: 200 }"

h1 = calc_hash(m1)
h2 = calc_hash(m2)
print("m1: %s, hash: 0x%s" % (m1,h1))
print("m2: %s, hash: 0x%s" % (m2,h2))

m3 = "{ a: 101, b: 200 }"
h3 = calc_hash(m3)
print("m3: %s, hash: 0x%s" % (m3,h3))
