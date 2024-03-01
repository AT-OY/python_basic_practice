import hashlib

m = hashlib.md5()
m.update(b"hello alex")
print(m.hexdigest())
m.update("欢迎来到小猿圈".encode("utf-8"))

# print(m.digest())
print(m.hexdigest())