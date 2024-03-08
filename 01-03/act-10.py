def get_user_input(list_name):
    while True:
        numbers = input(f"Enter numbers for {list_name}: ")
        num_list = [int(num) for num in numbers.split()]
        return num_list


def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list


list1 = get_user_input("list 1")
list2 = get_user_input("list 2")

merged_list = merge_and_sort_lists(list1, list2)
print("Merged and sorted list:", merged_list)
print("Smallest: ", merged_list[0])
print("Largest: ", merged_list[-1])
