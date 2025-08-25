print("📈Welcome to Stock Porfolio Tracker📈")

stock_prices={
    "AAPL":180, #Apple
    "TSLA":250, #Tesla
    "MSFT":300, #Microsoft
    "GOOGL":2800, #Google
    "AMZN":3400 #Amazon
}

print("----Available Stocks----")
for i,j in stock_prices.items():    
    print(i,":",j)
investment=0
while True:
    name=input("Enter Stock Name(or enter done to finish) : ").upper()
    if name=="DONE":
        break
    if name in stock_prices:
        quantity=int(input("Enter Stock Quantity : "))
        investment+=stock_prices[name]*quantity
        print("Shares added successfuly!")
    else:
        print("Stock Not Found!Please choose from the Availabe stocks.") 

print("Total Investment : ",investment)

with open("in_rslt.txt","a")as file:
    file.write(f"Total Investment : {investment}\n")
print("Investment details saved in the file")