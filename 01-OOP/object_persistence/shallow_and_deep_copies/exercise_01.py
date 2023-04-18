"""
1. Your task is to write a code that will prepare a proposal of reduced prices
   for the candies whose total weight exceeds 300 units of weight (we don’t
   care whether those are kilograms or pounds).

2. Your input is a list of dictionaries; each dictionary represents one type of
   candy. Each type of candy contains a key entitled "weight", which should
   lead you to the total weight details of the given delicacy. The input is
   presented in the editor;

3. Prepare a copy of the source list (this should be done with a one-liner)
   and then iterate over it to reduce the price of each delicacy by 20% if its
   weight exceeds the value of 300;

4. Present an original list of candies and a list that contains the proposals;

5. Check if your code works correctly when copying and modifying the candy item
   details.
"""
import copy


warehouse = list()
warehouse.append({"name": "Lolly Pop", "price": 0.4, "weight": 133})
warehouse.append({"name": "Licorice", "price": 0.1, "weight": 251})
warehouse.append({"name": "Chocolate", "price": 1, "weight": 601})
warehouse.append({"name": "Sours", "price": 0.01, "weight": 513})
warehouse.append({"name": "Hard candies", "price": 0.3, "weight": 433})
warehouse_original = copy.deepcopy(warehouse)

print("Source list of candies")
for item in warehouse:
    print(item)
    if item["weight"] > 300:
        item["price"] *= .8

print("*" * 10)
print("Source list of candies")
for item in warehouse:
    print(item)
