

# Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy.
# Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.

# Przykład użycia:
# >>> cash_machine = CashMachine()
# >>> cash_machine.is_available

# False

# >>> cash_machine.put_money([200, 100, 100, 50])
# >>> cash_machine.is_available()

# True

# >>> cash_machine.withdraw_money(150)
# [100, 50]

class TestCashMachine:
   def _init_(self):
       self._money = []

   def put_money(self, bills):
       self._money += bills

   @property
   def is_available(self):
       return len(self._money) > 0

   def withdraw_money(self, amout):
       to_withdraw = []

       for bill in sorted(self._money, reverse=True):
           if sum(to_withdraw) + bill <= amount:
               to_withdraw.append(bill)
       if sum(to_withdraw) == amount
           for bill in to_withdraw:
               self._money.remove(bill)
           return to_withdraw
       return []

class TestCashMachine:
    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_available_for_empty_machine(self):
        cash_machine = CashMachine()
        assert cash_machine.is_available is False

    def test_put_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True

    def test_withdraw_money(self):
        cash_machine - CashMachine()
        assert cash_machine.withdraw_money(150) == []
        # assert CashMachine.withdraw_money(cash_machine, 150) == []
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.withdraw_money(300) == [200, 100]

        cash_machine = CashMachine()
        cash_machine.put_money([50, 100, 100, 200])|
        assert cash_machine.withdraw_money(300) == [200, 100]
        assert cash_machine.withdraw_money(300) == []

        cash_machine = CashMachine()
