import numpy as np


def _to_string(a, b, c, z, x_b, x_n):
    str_ = _to_latex(a, b, c, z, x_b, x_n) \
        .replace(" ", "") \
        .replace("&", "") \
        .replace("\\\\", "") \
        .replace("\\hline", "--------------------")
    return "".join(map(lambda x: x + "\n", str_.split("\n")[1:-1]))


def _to_latex(a, b, c, z, x_b, x_n):
    result = "\\begin{array}{" + "r" * (3 + np.shape(c)[0] * 2) + "}\n"

    for i in range(np.shape(a)[0]):
        result += "    " + str(x_b[i]) + " & = & " + str(b[i])

        for j in range(np.shape(a)[1]):
            result += " & + & " if a[i, j] > 0 else " & - & " if a[i, j] < 0 else " &  & "
            result += str(abs(a[i, j])) if abs(a[i, j]) != 1 and a[i, j] != 0 else ""
            result += str(x_n[j]) if a[i, j] != 0 else ""

        result += " \\\\\n"

    result += "    \\hline\n"

    result += "    z & = & " + str(z)
    for j in range(np.shape(c)[0]):
        result += " & + & " if c[j] > 0 else " & - & " if c[j] < 0 else " &  & "
        result += str(abs(c[j])) if abs(c[j]) != 1 and c[j] != 0 else ""
        result += str(x_n[j]) if c[j] != 0 else ""

    result += "\n\\end{array}"
    return result


class Dictionary:
    def __init__(self, d, x_b, x_n):
        self.d = d
        self.x_b = x_b
        self.x_n = x_n

    def pivot_(self, entering, leaving):
        if not np.isin(entering, self.x_n):
            raise ValueError("Invalid entering variable")
        if not np.isin(leaving, self.x_b):
            raise ValueError("Invalid leaving variable")

        e_index = np.where(self.x_n == entering)[0][0]
        l_index = np.where(self.x_b == leaving)[0][0]

        self.x_b[l_index], self.x_n[e_index] = self.x_n[e_index], self.x_b[l_index]

        coefficient = self.d[l_index, e_index]
        self.d[l_index, e_index] = 1
        self.d[l_index, :] /= -coefficient

        coefficient = np.array([self.d[:, e_index]]).transpose()
        coefficient[l_index, :] = 0
        self.d += coefficient * self.d[l_index, :]
        self.d[:, e_index] -= coefficient[:, 0]

    def __str__(self):
        return _to_string(self.d[:-1, :-1], self.d[:-1, -1], self.d[-1, :-1], self.d[-1, -1], self.x_b, self.x_n)
