from fake_mafh import divide as fake_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
print(result1)
print(result2)

from true_math import divide as true_divide

result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result3)
print(result4)