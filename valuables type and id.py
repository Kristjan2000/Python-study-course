value1 = 1
value2 = "hii"


def type_and_id(value1, value2):
    print("Type of value1:", type(value1))
    print("Id of value1:", id(value1))
    print("Type of value2:", type(value2))
    print("Id of value2:", id(value2))
    if type(value1) == type(value2):
        print("True values match")
    else:
        print("values dont match")
    if id(value1) == id(value2):
        print("true id's match")
    else:
        print("id's dont match")

type_and_id(value1, value2)
