import pickle


a_dict = dict()
a_dict["EUR"] = {"code":"Euro", "symbol": "€"}
a_dict["GBP"] = {"code":"Pounds sterling", "symbol": "£"}
a_dict["USD"] = {"code":"US dollar", "symbol": "$"}
a_dict["JPY"] = {"code":"Japanese yen", "symbol": "¥"}

a_list = ["a", 123, [10, 100, 1000]]

with open("multidata.pckl", "wb") as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)

with open("multidata.pckl", "rb") as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)
