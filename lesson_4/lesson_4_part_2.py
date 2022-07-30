
integer = input("Какое количество учеников в 1-м математическом классе?")
class_1 = int(integer)

integer = input("Какое количество учеников в 2-м математическом классе?")
class_2 = int(integer)

integer = input("Какое количество учеников в 3-м математическом классе?")
class_3 = int(integer)

first_class_desks = (class_1 // 2) + (class_1 % 2)
second_class_desks = (class_2 // 2) + (class_2 % 2)
third_class_desks = (class_3 // 2) + (class_3 % 2)

total_desks = first_class_desks + second_class_desks + third_class_desks

print("Необходимо закупить", total_desks, "парт для всех учеников.")
