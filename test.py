def je_prastevilo(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prastevila_do(n):
    for i in range(1, n):
        if je_prastevilo(i) == True:
            print(i)

prastevila_do(200)