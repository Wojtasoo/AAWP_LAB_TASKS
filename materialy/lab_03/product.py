# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price >=0.0:
            self.price = price
        else:
            raise ValueError("Price cannot be negative")
        
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Quantity cannot be negative")
        
        if len(name) > 0:
            self.name = name
        else:
            raise ValueError("Name cannot be empty")
        
        

    def add_stock(self, amount: int):
        """Dodaje okreslona ilosc produktow do magazynu.

        Raises:
            ValueError: jesli amount jest ujemne
        """
        # TODO: Zaimplementuj dodawanie do magazynu
        if amount >= 0:
            self.quantity += amount
        else:
            raise ValueError("Amount cannot be negative")

    def remove_stock(self, amount: int):
        """Usuwa okreslona ilosc produktow z magazynu.

        Raises:
            ValueError: jesli amount jest ujemne lub wieksze niz dostepna ilosc
        """
        # TODO: Zaimplementuj usuwanie z magazynu
         # TODO: Zaimplementuj dodawanie do magazynu
        if amount < 0 or amount > self.quantity:
            raise ValueError("Amount cannot be negative")
        else:
            self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jesli produkt jest dostepny (quantity > 0)."""
        # TODO: Zaimplementuj sprawdzanie dostepnosci
        if self.quantity > 0:
            return True
        return False

    def total_value(self) -> float:
        """Zwraca calkowita wartosc produktow w magazynie (price * quantity)."""
        # TODO: Zaimplementuj obliczanie wartosci
        return self.price * self.quantity
    
    def apply_discount(self, percent: float):
        """Obniza cene o podany procent (0-100)."""
        # TODO: Zaimplementuj
        if percent not in range(0, 101):
            raise("Percentage can be only in range: 0-100")
        if percent == 100:
            self.price = 0
        elif percent > 0:
            self.price = self.price * (percent/100.0)
