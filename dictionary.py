import numpy as np


class Dictionary:
    def __init__(self, a, b, c, z, x_b, x_n):
        self.A = a
        self.b = b
        self.c = c
        self.z = z
        self.x_B = x_b
        self.x_N = x_n

    def pivot_(self, entering, leaving):
        if entering < 0 or entering >= np.shape(self.A)[1]:
            raise ValueError("Entering variable out of range")
        if leaving < 0 or leaving >= np.shape(self.A)[0]:
            raise ValueError("Leaving variable out of range")

        self.x_B[leaving], self.x_N[entering] = self.x_N[entering], self.x_B[leaving]

        coefficient = self.A[leaving, entering]
        self.A[leaving, :] /= -coefficient
        self.A[leaving, entering] /= -coefficient
        self.b[leaving] /= -coefficient

        coefficient = np.array([self.A[:, entering]]).transpose()
        coefficient[leaving, :] = 0
        self.A += coefficient * self.A[leaving, :]
        self.A[:, entering] -= coefficient[:, 0]
        self.b += coefficient[:, 0] * self.b[leaving]

        coefficient = self.c[entering]
        self.c += [coefficient * _ for _ in self.A[leaving, :]]
        self.c[entering] -= coefficient

        self.z += coefficient * self.b[leaving]

    def to_string(self):
        result = ""
        for i in range(np.shape(self.A)[0]):
            result += str(self.x_B[i]) + "=" + str(self.b[i])

            for j in range(np.shape(self.A)[1]):
                result += "+" if self.A[i, j] > 0 else ""
                result += str(self.A[i, j]) + str(self.x_N[j]) if self.A[i, j] != 0 else ""

            result += "\n"
        result += "--------------------\n"
        result += "z=" + str(self.z)
        for j in range(np.shape(self.c)[0]):
            result += "+" if self.c[j] > 0 else ""
            result += str(self.c[j]) + str(self.x_N[j]) if self.c[j] != 0 else ""

        return result

    def to_latex(self):
        result = "\\begin{array}{" + "r" * (3 + np.shape(self.c)[0] * 2) + "}\n"

        for i in range(np.shape(self.A)[0]):
            result += "    " + str(self.x_B[i]) + " & = & " + str(self.b[i])

            for j in range(np.shape(self.A)[1]):
                result += " & + & " if self.A[i, j] > 0 else " & - & "
                result += str(abs(self.A[i, j])) + str(self.x_N[j]) if self.A[i, j] != 0 else " &"

            result += "\n"

        result += "    \\hline\n"

        result += "    z & = & " + str(self.z)
        for j in range(np.shape(self.c)[0]):
            result += " & + & " if self.c[j] > 0 else " & - & "
            result += str(abs(self.c[j])) + str(self.x_N[j]) if self.c[j] != 0 else ""

        result += "\n\\end{array}"
        return result
