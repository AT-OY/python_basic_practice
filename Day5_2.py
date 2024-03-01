def dog(name, d_type):
    attack_vals = {
        "京巴": 30,
        "藏獒": 80
    }

    data = {
        "name": name,
        "d_type": d_type,
        # "attack_val": 30,
        "life_val": 100
    }
    if d_type in attack_vals:
        data["attack_val"] = attack_vals[d_type]
    else:
        data["attack_val"] = 15

    return data


def person(name, age):
    data = {
        "name": name,
        "age": age,
        "life_val": 100
    }
    if age > 18:
        data["attack_val"] = 50
    else:
        data["attack_val"] = 30

    return data


def dog_bit(dog_obj, person_obj):
    person_obj["life_val"] -= dog_obj["attack_val"]
    print("狗[%s]咬了人[%s]一口，人掉血[%s]，还有血量[%s]..." %
          (dog_obj["name"], person_obj["name"], dog_obj["attack_val"], person_obj["life_val"]))


def beat(person_obj, dog_obj):
    dog_obj["life_val"] -= person_obj["attack_val"]
    print("人[%s]打了狗[%s]一棒，狗掉血[%s]，还有血量[%s]..." %
          (person_obj["name"], dog_obj["name"], person_obj["attack_val"], dog_obj["life_val"]))


d1 = dog("mjj", "京巴")
d2 = dog("mjj2", "藏獒")

p1 = person("Alex", 22)

dog_bit(d1, p1)
beat(p1, d1)

print(d1)
print(d2)
print(p1)
