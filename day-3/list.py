#Shopping List

#Create a list
shopping_list = ["apples", "milk", "bread"]
print("Initial list:", shopping_list)

#Access the second item (index 1)
print("Second item:", shopping_list[1])

#Add item to the list
shopping_list.append("eggs")
print("After appending:", shopping_list)

#Change milk to almond milk
shopping_list[1] = "almond milk"
print("After Modifying:", shopping_list)

#Remove item
shopping_list.remove("apples")
print("After Modifying:", shopping_list)

#Print final length of the list
print("Length of list:", len(shopping_list))
