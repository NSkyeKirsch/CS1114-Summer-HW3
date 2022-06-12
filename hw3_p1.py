"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q1
Date due: 2022-06-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


def yards_to_miles(num_yards):
    """
    input: yards as a float
    :return: number of miles
    """

    return float(num_yards / 1760)


def main():
    solution_one = yards_to_miles(10000)
    solution_two = yards_to_miles(230012.23)
    solution_three = yards_to_miles(532823.932)

    print("one: {}, two: {}, three: {}".format(solution_one, solution_two, solution_three))


if __name__ == "__main__":
    main()
