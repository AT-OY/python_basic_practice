s = {
    "name": "Alex",
    "age": 18,
    "scores":{
        "语文": 130,
        "数学": 60,
        "英语": 98
    }
}

# s2 = s
# s2["name"] = "David"
# print(s["name"], s2["name"])

# s3 = s.copy()
# s3["name"] = "David"
# s3["scores"]["数学"] = 120
# print(s["name"], s3["name"])
# print(s["scores"]["数学"], s3["scores"]["数学"])

import copy
s4 = copy.deepcopy(s)
s4["name"] = "David"
s4["scores"]["数学"] = 120
print(s["name"], s4["name"])
print(s["scores"]["数学"], s4["scores"]["数学"])
