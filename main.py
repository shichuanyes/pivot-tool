import numpy as np
import rational
from dictionary import Dictionary
from rational import Rational

if __name__ == '__main__':
    # n = int(input("Enter the number of variables: "))
    # m = int(input("Enter the number of constrictions: "))
    #
    # str_ = input("Enter the coefficients for the objective function: ").strip().split()[:n + 1]
    # c = np.array([rational.from_str(_) for _ in str_])
    #
    # print("Enter the constraints: ")
    # a = np.empty((m, n + 1), Rational)
    # for i in range(m):
    #     str_ = np.array(input().strip().split()[:n + 1])
    #     a[i] = np.array([rational.from_str(_) for _ in str_])
    #
    # x_n = np.array(input("Enter the names for free variables: ").strip().split()[:n + 1])
    # x_b = np.array(input("Enter the names for slack variables: ").strip().split()[:m + 1])
    #
    # b = a[:, -1]
    # a = a[:, :-1]

    a = np.array([[Rational(1), Rational(0), Rational(7)],
                  [Rational(3), Rational(4), Rational(7)],
                  [Rational(5), Rational(6), Rational(0)]])
    x_b = np.array(["w_1", "w_2"])
    x_n = np.array(["x_1", "x_2"])

    d = Dictionary(a, x_b, x_n)

    print("The current dictionary is: \n")
    print(d)

    entering = input("Enter the entering variable (q to quit): ")
    if entering == "q":
        exit()
    leaving = input("Enter the leaving variable (q to quit): ")
    while leaving != "q":
        d.pivot_(entering, leaving)

        print("The current dictionary is: \n")
        print(d)

        entering = input("Enter the entering variable (q to quit): ")
        if entering == "q":
            exit()
        leaving = input("Enter the leaving variable (q to quit): ")
