import math

#implementando a aprox de pi
def aprox_pi(n):
    pi = float(0)
    for k in range (n):
        pi += 2*((2**k)*math.factorial(k)**2)/math.factorial(2*k+1)
    return pi

#implementando a aprox de e
def aprox_e():
    e = float(0)
    for k in range(5):
        e += 1/math.factorial(k)
    return e
