# Stock Portfolio Tracker (Basic)

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'exit' to stop): ").upper()
    
    if stock_name == 'EXIT':
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        
        print(f"Added {quantity} shares of {stock_name} worth ${investment}")
    else:
        print("Stock not found! Please choose from the list.")

print("\nTotal Investment Value: $", total_investment)

# Save result to file
with open("portfolio_result.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved to portfolio_result.txt")