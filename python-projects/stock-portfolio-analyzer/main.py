
# Beginner Stock Portfolio Analyzer
#
# This project uses plain Python to analyze a small stock portfolio.
# The data is manually entered so you can focus on Python basics first.


# A list stores multiple stock holdings.
# Each dictionary stores information about one holding.
portfolio = [
    {
        "ticker": "AAPL",
        "name": "Apple Inc.",
        "shares": 10,
        "average_purchase_price": 150.00,
        "current_price": 190.00,
    },
    {
        "ticker": "MSFT",
        "name": "Microsoft Corporation",
        "shares": 5,
        "average_purchase_price": 310.00,
        "current_price": 425.00,
    },
    {
        "ticker": "KO",
        "name": "Coca-Cola Company",
        "shares": 20,
        "average_purchase_price": 62.00,
        "current_price": 60.00,
    },
    {
        "ticker": "VOO",
        "name": "Vanguard S&P 500 ETF",
        "shares": 3,
        "average_purchase_price": 420.00,
        "current_price": 500.00,
    },
]


# This function calculates how much money was originally invested.
def calculate_cost_basis(shares, average_purchase_price):
    return shares * average_purchase_price


# This function calculates what the holding is worth today.
def calculate_market_value(shares, current_price):
    return shares * current_price


# This function calculates the dollar profit or loss.
def calculate_gain_loss(market_value, cost_basis):
    return market_value - cost_basis


# This function calculates the percentage return on the investment.
def calculate_percentage_return(gain_loss, cost_basis):
    return (gain_loss / cost_basis) * 100


# This function calculates how much of the total portfolio value
# comes from one holding.
def calculate_allocation(market_value, total_portfolio_value):
    return (market_value / total_portfolio_value) * 100


# These variables keep track of portfolio totals.
total_cost_basis = 0
total_market_value = 0


# First loop: calculate total cost basis and total market value.
# We need the total market value before we can calculate allocations.
for stock in portfolio:
    cost_basis = calculate_cost_basis(
        stock["shares"],
        stock["average_purchase_price"],
    )
    market_value = calculate_market_value(
        stock["shares"],
        stock["current_price"],
    )

    total_cost_basis += cost_basis
    total_market_value += market_value


# These variables will help us find the best and worst performers.
best_holding = None
worst_holding = None
best_return = None
worst_return = None


print("BEGINNER STOCK PORTFOLIO ANALYZER")
print("=" * 40)
print()


# Second loop: analyze and print each individual stock holding.
for stock in portfolio:
    cost_basis = calculate_cost_basis(
        stock["shares"],
        stock["average_purchase_price"],
    )
    market_value = calculate_market_value(
        stock["shares"],
        stock["current_price"],
    )
    gain_loss = calculate_gain_loss(market_value, cost_basis)
    percentage_return = calculate_percentage_return(gain_loss, cost_basis)
    allocation = calculate_allocation(market_value, total_market_value)

    # Store calculated results back inside the dictionary.
    # This makes it easier to use the results later if needed.
    stock["cost_basis"] = cost_basis
    stock["market_value"] = market_value
    stock["gain_loss"] = gain_loss
    stock["percentage_return"] = percentage_return
    stock["allocation"] = allocation

    # Check if this stock is the best performer so far.
    if best_return is None or percentage_return > best_return:
        best_holding = stock
        best_return = percentage_return

    # Check if this stock is the worst performer so far.
    if worst_return is None or percentage_return < worst_return:
        worst_holding = stock
        worst_return = percentage_return

    print(f"Ticker: {stock['ticker']}")
    print(f"Name: {stock['name']}")
    print(f"Shares Owned: {stock['shares']}")
    print(f"Average Purchase Price: ${stock['average_purchase_price']:.2f}")
    print(f"Current Price: ${stock['current_price']:.2f}")
    print(f"Cost Basis: ${cost_basis:.2f}")
    print(f"Current Market Value: ${market_value:.2f}")
    print(f"Gain/Loss: ${gain_loss:.2f}")
    print(f"Percentage Return: {percentage_return:.2f}%")
    print(f"Portfolio Allocation: {allocation:.2f}%")
    print("-" * 40)


# Calculate overall portfolio gain or loss.
total_gain_loss = calculate_gain_loss(total_market_value, total_cost_basis)
total_percentage_return = calculate_percentage_return(
    total_gain_loss,
    total_cost_basis,
)


print()
print("PORTFOLIO SUMMARY")
print("=" * 40)
print(f"Total Cost Basis: ${total_cost_basis:.2f}")
print(f"Total Current Portfolio Value: ${total_market_value:.2f}")
print(f"Total Portfolio Gain/Loss: ${total_gain_loss:.2f}")
print(f"Total Portfolio Return: {total_percentage_return:.2f}%")
print()

print("PERFORMANCE SUMMARY")
print("=" * 40)
print(
    f"Best Performer: {best_holding['ticker']} "
    f"({best_holding['percentage_return']:.2f}%)"
)
print(
    f"Worst Performer: {worst_holding['ticker']} "
    f"({worst_holding['percentage_return']:.2f}%)"
)
