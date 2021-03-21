import numpy as np
from dictionary import Dictionary
from rational import Rational

if __name__ == '__main__':
    n = int(input("Enter the number of variables: "))
    m = int(input("Enter the number of constrictions: "))

    s = np.array(input("Enter the coefficients for the objective function: ").strip().split()[:n + 1])
    c = np.empty(n, Rational)
    for i in range(np.shape(s)[0]):
        p = [int(t) for t in s[i].split("/")]
        c[i] = Rational(p[0], p[1] if len(p) > 1 else 1)

    print("Enter the constraints: ")
    A = np.empty((m, n + 1), Rational)
    for i in range(m):
        s = np.array(input().strip().split()[:n + 1])
        for j in range(np.shape(s)[0]):
            p = [int(t) for t in s[i].split("/")]
            A[i, j] = Rational(p[0], p[1] if len(p) > 1 else 1)

    x_N = np.array(list(map(str, input("Enter the names for free variables: ").strip().split()))[:n + 1])
    x_B = np.array(list(map(str, input("Enter the names for slack variables: ").strip().split()))[:m + 1])

    b = A[:, -1]
    A = A[:, :-1]

    # A = np.array([[Rational(1), Rational(2)], [Rational(3), Rational(4)]])
    # b = np.array([Rational(7), Rational(8)])
    # c = np.array([Rational(5), Rational(6)])
    # x_B = np.array(["w_1", "w_2"])
    # x_N = np.array(["x_1", "x_2"])

    d = Dictionary(A, b, c, Rational(0), x_B, x_N)

    print("The current dictionary is: \n")
    print(d.to_string())

    entering = input("Enter the entering variable (q to quit):")
    if entering == "q":
        exit()
    leaving = input("Enter the leaving variable (q to quit): ")
    while leaving != "q":
        entering_index = np.where(d.x_N == entering)
        leaving_index = np.where(d.x_B == leaving)

        d.pivot_(entering_index[0][0], leaving_index[0][0])

        print("The current dictionary is: \n")
        print(d.to_string())

        entering = input("Enter the entering variable (q to quit): ")
        if entering == "q":
            exit()
        leaving = input("Enter the leaving variable (q to quit): ")
