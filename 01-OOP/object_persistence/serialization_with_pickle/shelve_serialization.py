import shelve


db_name = "data.shlv"

shelve_db = shelve.open(db_name, flag="c")

shelve_db["53722548E"] = {
    "name": "Sergio",
    "lastname": "Díaz Martínez",
    "birthdate": "1989-03-1989",
}
shelve_db.close()

shelve_db = shelve.open(db_name, flag="r")

# is possible make use of dictionary utilities
print(type(shelve_db["53722548E"]))
print("53722548E" in shelve_db)
print(shelve_db["53722548E"].keys())
print(shelve_db["53722548E"].items())
del shelve_db["53722548E"]["lastname"]

print(shelve_db["53722548E"])
shelve_db.close()
