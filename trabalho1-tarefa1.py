import math

pi_exato = math.pi
e_exato = math.e

#implementando a aprox de pi
def aprox_pi(n):
    pi = float(0)
    for k in range (n):
        pi += 2*((2**k)*math.factorial(k)**2)/math.factorial(2*k+1)
    return pi

#implementando a aprox de e
def aprox_e(n):
    e = float(0)
    for k in range(n):
        e += 1/math.factorial(k)
    return e

#comparando pi
## n = 5
erro_pi = abs(pi_exato - aprox_pi(5))
print('****** n = 5 ******')
print(f"Aproximação de pi = {aprox_pi(5):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.10f}")

import math

pi_exato = math.pi
e_exato = math.e

#implementando a aprox de pi
def aprox_pi(n):
    pi = float(0)
    for k in range (n):
        pi += 2*((2**k)*math.factorial(k)**2)/math.factorial(2*k+1)
    return pi

#implementando a aprox de e
def aprox_e(n):
    e = float(0)
    for k in range(n):
        e += 1/math.factorial(k)
    return e

#comparando pi
## n = 5
erro_pi = abs(pi_exato - aprox_pi(5))
print('****** n = 5 ******')
print(f"Aproximação de pi = {aprox_pi(5):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.10f}")

## n = 10
erro_pi = abs(pi_exato - aprox_pi(10))
print('****** n = 10 ******')
print(f"Aproximação de pi = {aprox_pi(10):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.10f}")

## n = 50
erro_pi = abs(pi_exato - aprox_pi(50))
print('****** n = 50 ******')
print(f"Aproximação de pi = {aprox_pi(50):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.20f}")

## n = 100
erro_pi = abs(pi_exato - aprox_pi(100))
print('****** n = 100 ******')
print(f"Aproximação de pi = {aprox_pi(100):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.20f}")

## n = 500
erro_pi = abs(pi_exato - aprox_pi(500))
print('****** n = 500 ******')
print(f"Aproximação de pi = {aprox_pi(500):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.20f}")

## n = 1000
erro_pi = abs(pi_exato - aprox_pi(1000))
print('****** n = 1000 ******')
print(f"Aproximação de pi = {aprox_pi(1000):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.20f}")

## n = 5000
erro_pi = abs(pi_exato - aprox_pi(5000))
print('****** n = 5000 ******')
print(f"Aproximação de pi = {aprox_pi(5000):.10f}")
print(f"Erro absoluto de pi = {erro_pi:.20f}")


print('------------------------------------------------------')

#comparando e
## n = 5
erro_e = abs(e_exato - aprox_e(5))
print('****** n = 5 ******')
print(f"Aproximação de e = {aprox_e(5):.10f}")
print(f"Erro absoluto de e = {erro_e:.10f}")

## n = 10
erro_e = abs(e_exato - aprox_e(10))
print('****** n = 10 ******')
print(f"Aproximação de e = {aprox_e(10):.10f}")
print(f"Erro absoluto de e = {erro_e:.10f}")

## n = 50
erro_e = abs(e_exato - aprox_e(50))
print('****** n = 50 ******')
print(f"Aproximação de e = {aprox_e(50):.10f}")
print(f"Erro absoluto de e = {erro_e:.20f}")

## n = 100
erro_e = abs(e_exato - aprox_e(100))
print('****** n = 100 ******')
print(f"Aproximação de e = {aprox_e(100):.10f}")
print(f"Erro absoluto de e = {erro_e:.20f}")

## n = 500
erro_e = abs(e_exato - aprox_e(500))
print('****** n = 500 ******')
print(f"Aproximação de e = {aprox_e(500):.10f}")
print(f"Erro absoluto de e = {erro_e:.20f}")

## n = 1000
erro_e = abs(e_exato - aprox_e(1000))
print('****** n = 1000 ******')
print(f"Aproximação de e = {aprox_e(1000):.10f}")
print(f"Erro absoluto de e = {erro_e:.20f}")

## n = 5000
erro_e = abs(e_exato - aprox_e(5000))
print('****** n = 5000 ******')
print(f"Aproximação de e = {aprox_e(5000):.10f}")
print(f"Erro absoluto de e = {erro_e:.20f}")
