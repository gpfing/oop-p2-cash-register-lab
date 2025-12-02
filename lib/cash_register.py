#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, items=[], previous_transactions=[]):
    self.total = 0
    self.discount = discount
    self.items = []
    self.previous_transactions = []

    @property
    def discount(self):
      return self._discount
    @discount.setter
    def discount(self, value):
      if type(value) is int and 100 >= value >= 0:
        self._discount = value
      else:
        raise ValueError("Not valid discount.")
      
  def add_item(self, item, price, quantity=1):
    for i in range(quantity):
      self.items.append(item)
    self.total += price * quantity
    self.previous_transactions.append({"item": item, "price": price * quantity, "quantity": quantity})

  def apply_discount(self):
    if len(self.previous_transactions) > 0 and self.discount > 0:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      new_transaction_item = {"item":self.previous_transactions[-1]["item"],
                                "price": self.previous_transactions[-1]["price"] - discount_amount,
                                  "quantity": self.previous_transactions[-1]["quantity"]}
      self.previous_transactions.pop()
      self.previous_transactions.append(new_transaction_item)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      self.void_last_transaction()
      print("There is no discount to apply.")
    

  def void_last_transaction(self):
    if len(self.previous_transactions) > 0:
      last_transaction = self.previous_transactions[-1]
      self.previous_transactions.pop()
      self.total -= last_transaction["price"]
    else:
      self.total = 0
