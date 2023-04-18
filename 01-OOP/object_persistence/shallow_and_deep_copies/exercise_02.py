"""
1. introduce the Delicacy class to represent a generic delicacy. The objects of
   this class will replace the old school dictionaries. Suggested attribute
   names: name, price, weight;

2. your class should implement the __str__() method to represent each object
   state;

3. experiment with the copy.copy() and deepcopy.copy() methods to see the
   difference in how each method copies objects.
"""
import copy


class Delicacy:
   def __init__(self, name: str, price: float, weight: int) -> None:
      self.name = name
      self.price = price
      self.weight = weight

   def __str__(self) -> str:
      return f"Name: {self.name}\nPrice: {self.price}\nWeight: {self.weight}\n"


if __name__ == "__main__":
   obj_list = [
      Delicacy(name="Lolly Pop", price=0.4, weight=133),
      Delicacy(name="Licorice", price=0.1, weight=251),
      Delicacy(name="Chocolate",price=1, weight=601),
      Delicacy(name="Sours", price=0.01, weight=513),
      Delicacy(name="Hard candies", price=0.3, weight=433),
   ]
   original_copy_list = copy.deepcopy(obj_list)

   print("Source list of candies")
   for item in obj_list:
      print(item)
      if item.weight > 300:
         item.price *= .8

   print("*" * 10)
   print("Source list of candies")
   for item in obj_list:
      print(item)
