# # Python code to
# # demonstrate readlines()
#
# L = ["Geeks\n", "for\n", "Geeks\n"]
#
#
#
# # Using readlines()
# file1 = open(r'C:\oscillation.txt', 'r')
# Lines = file1.readlines()
# oscillation = []
#
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     # oscillation.append(line)
#     # print(oscillation)
#     print("Line{}: {}".format(count, line.strip()))


with open(r'C:\oscillation.txt', 'r') as grilled_cheese:
	lines = grilled_cheese.readlines()

	quantities = []
	ingredients = []

	for l in lines:
            as_list = l.split(", ")
            quantities.append(as_list[0])
            ingredients.append(as_list[1].replace("\n", ""))

	print(quantities)
	print(ingredients)