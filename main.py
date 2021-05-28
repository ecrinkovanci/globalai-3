students_passing_lists = []


notes1 = {"midterm grade": float(input("enter your midterm grade (for first student): ")),
"project grade": float(input("enter your project grade (for first student): ")),
"final grade": float(input("enter your final grade (for first student): ")),
}
notes1["passing grade"] = (notes1["midterm grade"] * 0.3) + (notes1["project grade"] * 0.3) + (notes1["final grade"] * 0.4)

students_passing_lists.append(notes1["passing grade"])


notes2 = {"midterm grade": float(input("enter your midterm grade (for second student): ")),
"project grade": float(input("enter your project grade (for second student): ")),
"final grade": float(input("enter your final grade (for second student): ")),
}
notes2["passing grade"] = (notes2["midterm grade"] * 0.3) + (notes2["project grade"] * 0.3) + (notes2["final grade"] * 0.4)

students_passing_lists.append(notes2["passing grade"])


notes3 = {"midterm grade": float(input("enter your midterm grade (for third student): ")),
"project grade": float(input("enter your project grade (for third student): ")),
"final grade": float(input("enter your final grade (for third student): ")),
}
notes3["passing grade"] = (notes3["midterm grade"] * 0.3) + (notes3["project grade"] * 0.3) + (notes3["final grade"] * 0.4)

students_passing_lists.append(notes3["passing grade"])


notes4 = {"midterm grade": float(input("enter your midterm grade (for fourth student): ")),
"project grade": float(input("enter your project grade (for fourth student): ")),
"final grade": float(input("enter your final grade (for fourth student): ")),
}
notes4["passing grade"] = (notes4["midterm grade"] * 0.3) + (notes4["project grade"] * 0.3) + (notes4["final grade"] * 0.4)

students_passing_lists.append(notes4["passing grade"])


notes5 = {"midterm grade": float(input("enter your midterm grade (for fifth student): ")),
"project grade": float(input("enter your project grade (for fifth student): ")),
"final grade": float(input("enter your final grade (for fifth student): ")),
}
notes5["passing grade"] = (notes5["midterm grade"] * 0.3) + (notes5["project grade"] * 0.3) + (notes5["final grade"] * 0.4)

students_passing_lists.append(notes5["passing grade"])


students_passing_lists.sort()

print(students_passing_lists[::-1])
