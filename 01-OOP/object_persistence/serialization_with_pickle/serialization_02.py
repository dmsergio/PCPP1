import pickle


a_list = ["a", 123, [10, 100, 1000]]
obj_bytes = pickle.dumps(a_list)
print("Intermediate object type, used to preserve data:", type(obj_bytes))

# now pass "obj_bytes" to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(obj_bytes)
print("A type of deserialized object:", type(b_list))
print("Contents:", b_list)
