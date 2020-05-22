

# Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee.
# Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi.

# >>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.give_bonus(1000.0)
# >>> employee.pay_salary()


class Employee:

    def __init_(selfself, first_name, last_name, rate, rate_per_hour):
        self.registered_time = 0
        self.first_name = first_name
        self.last_name = last_name
        self,rate_per_hour = rate_per_hour

    def register_time(self,hours):
        self.registered_time = hours

    def pay_salary(self):
        if self.registered_time <= 8:
            to_pay = self.registered_time * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.registered_time - 8) * self.rate_per_hour * 2
            self.registered_time = 8
            return to_pay

class PremiumEmployee(Employee):

    def __init_(self, first_name, last_name, rate_per_hour):
        super().__init__(first_name, last_name, rate_perhour)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += 0

    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonus
        self.bonus = 0
        return to_pay

class TestPremiumEmployee:
    def test_init(self):
        pe = PremiumEmployee("Jan", "Nowak", 100.00)
        assert pe
        assert isinstance(pe, PremiumEmployee)
        assert isinstance(pe, Employee)

    def test_give_bonus_and_pay_salary(self):
        pe = PremiumEmployee("Jan", "Nowak", 100.00)
        pe.register_time(5)
        pe.give_bonus(1000)
        assert pe.pay_salary() == 100 * 5 + 1000
        assert pe.pay_salary() == 0