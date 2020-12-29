from main import ADT
import random

size_of_list = 10
adt_obj = ADT(size_of_list)
for i in range(size_of_list-2):
    value = random.randint(0, 10)
    adt_obj.AppendIn(value)

adt_obj.Display()
print("__"*10)

print(f"Total Sum : {adt_obj.Sum()}")
print("Total Average : %.2f" % adt_obj.Average())
print("Max Value is : %.df" % adt_obj.Max())
print("Min Value is : %.df" % adt_obj.Min())
print(f"\n\nReversed array ")
adt_obj.ReverseArray()


number_of_rotation = random.randint(15, 120)
print(f"\n\nRotated Array Left {number_of_rotation} (times) ")
for i in range(number_of_rotation):
    adt_obj.RotateLeft()
adt_obj.Display()
