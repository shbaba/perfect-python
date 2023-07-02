from decimal import Decimal

print(0.1 == Decimal("0.1"))

print("----------")
print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 == 0.3)

print("----------")
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))

print("---------")
print(Decimal("1.50") + Decimal("2.50"))
print(Decimal("1.50") * Decimal("2.50"))


