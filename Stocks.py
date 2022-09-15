#Maheen Hanif Ghaffar
#Stocks 

#Inputs:
SharesPurchased = int(2000)
PricePerShare = float(40.00)
SharesSold = int(2000)
PriceSoldPerShare = float(42.75)

#Calculations:
PurchasePrice = SharesPurchased * PricePerShare
CommissionOnPurchase = PurchasePrice * 3/100
SellingPrice = SharesSold * PriceSoldPerShare
CommissionOnSale = SellingPrice * 3/100 
Profit = SellingPrice - PurchasePrice - CommissionOnPurchase - CommissionOnSale

#Print:
print(f"The amount of money Joe paid for the stock is: ${PurchasePrice:,.2f}")
print(f"The amount of commission Joe paid his broker when he bought the stock is: ${CommissionOnPurchase:,.2f}")
print(f"The amount for which Joe sold the stock is: ${SellingPrice:,.2f}")
print(f"The amount of commission Joe paid his broker when he sold the stock is: ${CommissionOnSale:,.2f}")
print(f"The profit that Joe had after selling the stocks is: ${Profit:,.2f}")
