'''def find_first_difference_index(list1, list2):
    for i, (elem1, elem2) in enumerate(zip(list1, list2)):
        if elem1 != elem2:
            return i
    return None  # If lists are identical

def main():
    # Input lists
    list1 = [int(x) for x in input("Enter the first list separated by spaces: ").split()]
    list2 = [int(x) for x in input("Enter the second list separated by spaces: ").split()]

    # Check if lists are of equal size
    if len(list1) != len(list2):
        print("Error: Lists must be of equal size.")
        return

    # Find the first index where the lists differ
    diff_index = find_first_difference_index(list1, list2)

    if diff_index is not None:
        print(f"The lists differ at index {diff_index}.")
    else:
        print("The lists are identical.")

if __name__ == "__main__":
    main()
'''


print("Enter two equal sized lists")
l1 = eval(input("Enter first list: "))
l2 = eval(input("Enter second list: "))

for i in range(len(l1)):
    if l1[i] != l2[i]:
        print("Lists differ at index", i)
        break
else:
    print("Lists are equal")