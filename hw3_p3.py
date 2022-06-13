"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q3
Date due: 2022-06-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random


def my_shuffle(old_list):
    """
    :param old_list: a list in any order
    :return new_list: new list in random order
    """
    new_list = []
    for i in range(len(old_list)):
        new_index = random.randint(0, len(old_list)-1)
        new_list.append(old_list[new_index])
        old_list.pop(new_index)

    return new_list


def main():
    print(my_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(my_shuffle([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]))
    print(my_shuffle(['Tandon', 'Tisch', 'Stern', 'Gallatin', 'Meyers', 'Steinhardt']))


if __name__ == "__main__":
    main()
