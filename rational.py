import math


class Rational:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError()
        elif denominator > 0:
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = -numerator
            self.denominator = -denominator

    def __str__(self):
        return "{}".format(self.numerator) if self.denominator == 1 or self.numerator == 0 \
            else "{}/{}".format(self.numerator, self.denominator)

    def __repr__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other):
        if isinstance(other, int):
            return self.__add__(Rational(other))
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator).reduce()

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__mul__(Rational(other))
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator).reduce()

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.__truediv__(Rational(other))
        if isinstance(other, Rational):
            return self.__mul__(other.inverse())

    def __eq__(self, other):
        if isinstance(other, int):
            return self.__eq__(Rational(other))
        if isinstance(other, Rational):
            return self.numerator * other.denominator == other.numerator * self.denominator

    def __gt__(self, other):
        if isinstance(other, int):
            return self.__gt__(Rational(other))
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        if isinstance(other, int):
            return self.__lt__(Rational(other))
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def inverse(self):
        return Rational(self.denominator, self.numerator)

    def inverse_(self):
        self.numerator, self.denominator = self.denominator, self.numerator

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return Rational(self.numerator // gcd, self.denominator // gcd)

    def reduce_(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def value(self):
        return self.numerator * 1.0 / self.denominator


def from_str(str_: str):
    p = [int(t) for t in str_.split("/")]
    return Rational(p[0], p[1] if len(p) > 1 else 1)
