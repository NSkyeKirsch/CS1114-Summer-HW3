"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q5
Date due: 2022-06-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


def largest_of_the_three(three_floats):
    """
    :param three_floats: a tuple of three floats or ints
    :return: largest value in the tuple
    """
    biggest = three_floats[0]
    for num in three_floats:
        if num > biggest:
            biggest = num

    return biggest


def main():
    print(largest_of_the_three((1, 2, 3)))
    print(largest_of_the_three((4.56, 0.12, 1.312)))
    print(largest_of_the_three((5, 5, 2)))


if __name__ == "__main__":
    main()
