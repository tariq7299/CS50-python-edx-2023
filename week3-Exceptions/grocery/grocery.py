
# The first Method--(cleaner method)
from collections import defaultdict

# Using a dictionary instead of a list
GROCERY_DICT = defaultdict(int)

def main():
    # Main function to read user input, add items to the grocery list,
    # and display the sorted grocery list.
    while True:
        try:
            item = input().strip().upper()
            add_item_to_grocery_list(item)
        except EOFError:
            display_grocery_list()
            return

def add_item_to_grocery_list(item):

    # Add the item to the grocery list and update its count if it already exists.
    # This is one of the benefits of using defaultdict() method
    GROCERY_DICT[item] += 1

def display_grocery_list():
    # Display the sorted grocery list with item counts.
    if not GROCERY_DICT:
        print('No items were entered!')
        return

    # .items() is necessary to convert GROCERY_DICT to a LIST, on order to be able to sort it
    sorted_items = sorted(GROCERY_DICT.items(), key=lambda x: x[0])

    # (sorted_items) returns a list of tuples
    for item, count in sorted_items:
        print(f'{count} {item}')

main()

# Second Method, simpler but not cleaner (or maybe not even simpler)
# GROCERY_LIST = []

# def main():

#     while True:
#         try:
#             item = input().strip().upper()
#             add_item_to_grocery_list(item)
#         except EOFError:
#             if len(GROCERY_LIST) == 0:
#                 print('No items were entered !')
#                 return
#             else:
#                 GROCERY_LIST.sort(key=lambda item_in_list: item_in_list['name'])
#                 for item_in_list in GROCERY_LIST:
#                     print(item_in_list['count'], item_in_list['name'])
#                 return

# def add_item_to_grocery_list(item):
#     for item_in_list in GROCERY_LIST:
#         if item == item_in_list["name"]:
#             item_in_list["count"] += 1
#             return
#     new_item = {'name':item, 'count':1}
#     GROCERY_LIST.append(new_item)
#     return
# main()
