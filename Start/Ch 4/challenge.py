# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self):
        pass

@dataclass
class Stock(Asset):
    ticker: str
    company: str

    def __lt__(self, other):
        return self.price < other.price

@dataclass
class Bond(Asset):
    description: str
    duration: int
    yieldamt: float

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt
        
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock(ticker="MSFT", price=342.0, company="Microsoft Corp"),
    Stock(ticker="GOOG", price=135.0, company="Google Inc"),
    Stock(ticker="META", price=275.0, company="Meta Platforms Inc"),
    Stock(ticker="AMZN", price=120.0, company="Amazon Inc")
]

bonds = [
    Bond(price=95.31, description="30 Year US Treasury", duration=30, yieldamt=4.38),
    Bond(price=96.70, description="10 Year US Treasury", duration=10, yieldamt=4.28),
    Bond(price=98.65, description="5 Year US Treasury", duration=5, yieldamt=4.43),
    Bond(price=99.57, description="2 Year US Treasury", duration=2, yieldamt=4.98)

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)
