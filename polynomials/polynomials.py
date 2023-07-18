from numbers import Number
from numbers import Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    def __sub__(self,other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                 other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:]) #do I need comma after other? YES OTHERWISE FIRST TERM IS NOT A TUPLE
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        return self - other
    
    def __mul__(self,other):
        if isinstance(other, Number):
            coefs = tuple(a * other for a in self.coefficients)
            return Polynomial(coefs)
        
        elif isinstance(other, Polynomial):
            oldpoly = Polynomial((0,))
            for count, a in enumerate(self.coefficients):
                coefs = tuple(a*b for b in other.coefficients) 
                newcoef = (0,)*count + coefs
                poly = Polynomial(newcoef) + oldpoly
                oldpoly = poly
            return poly
        
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self * other
    
    def __pow__(self, other):

        if isinstance(other, Integral):
            poly = Polynomial((1,))
            for i in range(other):
                poly = self * poly
            return poly
        
        else:
            return NotImplemented
        
    def __call__(self, other):

        if isinstance(other, Number):
            value = 0
            for count, a in enumerate(self.coefficients):
                value = value + a*(other ** count)
            return value
    
        else:
            return NotImplemented
    
    def dx(self):
        if isinstance(self, Polynomial):
            coefs = tuple(a*b for a,b in enumerate(self.coefficients))
            poly = coefs[1:]
            return Polynomial(poly)
        else:
            return NotImplemented
