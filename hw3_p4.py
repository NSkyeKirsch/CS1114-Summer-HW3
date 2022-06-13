"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q4
Date due: 2022-06-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def add_list(list1, list2):
    """
    input: two lists of the same length
    :param list1:
    :param list2:
    :return: sum of the first numbers, sum of the seconds numbers... etc
    """

    new_list = [item_1 + item_2 for item_1 in list1 for item_2 in list2 if list1.index(item_1) == list2.index(item_2)]

    return new_list


def create_list(keyword):
    inp = 0
    new_lst = []
    print("Enter values of the {} list of integers, one per line. Enter ‘done’ to finish this list.".format(keyword))
    while inp != "done":
        inp = input("")
        if inp != "done":
            new_lst.append(int(inp))
    return new_lst


def main():
    inp = 0
    list_1 = create_list("first")
    list_2 = create_list("second")

    if len(list_1) == len(list_2):
        print("The resulting list is: {}".format(add_list(list_1, list_2)))
    else:
        print("The lists are different lengths.")



if __name__ == "__main__":
    main()