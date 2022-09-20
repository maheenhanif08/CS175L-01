#Maheen Hanif Ghaffar
#Stocks 

#Inputs:
SharesPurchased = float(input("Enter the number of shares purchased: "))
PricePerShare = float(input("Enter the price per share: "))
SharesSold = float(input("Emter the mumber of shares sold: "))
PriceSoldPerShare = float(input("Enter the selling price per share: "))

#Calculations:
PurchasePrice = SharesPurchased * PricePerShare
CommissionOnPurchase = PurchasePrice * 3/100
SellingPrice = SharesSold * PriceSoldPerShare
CommissionOnSale = SellingPrice * 3/100 
Profit = SellingPrice - PurchasePrice - CommissionOnPurchase - CommissionOnSale

#Print:
print(f"Amount paid for stock: ${PurchasePrice:,.2f}")
print(f"Commission paid on the purchase: ${CommissionOnPurchase:,.2f}")
print(f"Amount the stock is sold for: ${SellingPrice:,.2f}")
print(f"Commission paid on the sale: ${CommissionOnSale:,.2f}")
print(f"Profit (or loss if negative): ${Profit:,.2f}")
