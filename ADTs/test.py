from main import ADT
import random

# Insert value in the ADT
# size_of_list = 5
# adt_obj = ADT(size_of_list)
# for i in range(size_of_list):
#     value = random.randint(0, 10)
#     adt_obj.AppendIn(value)
# adt_obj.Display()
# print("\n\n")
# adt_obj.RotateRight(3)


# print(f"Total Sum : {adt_obj.Sum()}")
# print("Total Average : %.2f" % adt_obj.Average())
# print("Max Value is : %.df" % adt_obj.Max())
# print("Min Value is : %.df" % adt_obj.Min())
# print(f"\n\nReversed array ")
# adt_obj.ReverseArray()


# number_of_rotation = random.randint(15, 120)
# print(f"\n\nRotated Array Left {number_of_rotation} (times) ")
# for i in range(number_of_rotation):
#     adt_obj.RotateLeft()
# adt_obj.Display()

random.seed(1)
l = [random.randint(-100, 100) for i in range(110)]
obj = ADT(l)
obj.Display()
print(f"\n\n")
obj.NegativePositiveSeprator()
