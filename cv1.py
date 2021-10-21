#!/usr/bin/env python3

class Pozdrav:
        def __init__(self, paMeno):
            self.aPozdravEN = "Hello"
            self.aPozdravSK = "Cus"

        def pozdravMa(self, paJazyk):
            if paJazyk == "EN":
                return self.aPozdravEN + " " + self.aMeno
            if paJazyk == "SK":
                return self.aPozdravSK + " " + self.aMeno 

jazyk = input("Choose your language/Vyber si svoj jazyk")
meno = input("Enter your name/Zadaj svoje meno")

hello = Pozdrav(meno)

pozdrav = hello.pozdravMa(jazyk)

print(pozdrav)