class payment:

    raise_amount = 1.03

    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    @classmethod
    def set_class_amount(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount


p1 = payment(1.5)
p2 = payment(1.21)
print(p1.amount)
print(p1.raise_amount)
print(p2.amount)
print(p2.raise_amount)

payment.set_class_amount(1.05)
print(payment.raise_amount)
print(p1.raise_amount)
print(p2.raise_amount)