SharesPurchased = int(2000)
PricePerShare = float(40.00)
SharesSold = int(2000)
PriceSoldPerShare = float(42.75)

OverallPrice = SharesPurchased * PricePerShare
Commission = OverallPrice * 3/100
SellingPrice = SharesSold * PriceSoldPerShare

print("The amount of money Joe paid for the stock is:", OverallPrice)
print("The amount of commission Joe paid his broker when he bought the stock is:", Commission)
print("The amount for which Joe sold the stock is:", SellingPrice)
