import yfinance as yf # type: ignore
import json
portfolio={}

def stockdata_get(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_history = stock.history(period='1d')
        if stock_history.empty:
            print(f"No information available for the ticker: {ticker}.")
            return None
        return stock_history
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def add_stockdata(ticker,share,price_purchase):
    if ticker in portfolio:
        print(f"Ticker {ticker} already exists in portfolio. Updating the shares and prices...")
        portfolio[ticker]["shares"]+=share
        portfolio[ticker]["purchase_price"]=price_purchase
    else:
        data=stockdata_get(ticker)
        if data is None:
            print(f"Could not shares: {share} and purchase price: {price_purchase} of ticker: {ticker} to the portfolio.")
            return None
        portfolio[ticker]={
            "shares":share,
            "purchase_price":price_purchase
            }
        print(f"Succesfully added shares: {share} to the ticker: {ticker} at a purchase price: {price_purchase}.")

def remove_stockdata(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Successfully removed data fot ticker: {ticker} from portfolio.")
    print(f"Couldn't find data for ticker: {ticker}to remove.")
    return None

def display_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
        return
    total_performance = 0
    for ticker,values in portfolio.items():
        data = stockdata_get(ticker)
        if data is None:
            continue
        current_price = data['Close'][-1]
        share_no = values["shares"]
        purchaseprice = values["purchase_price"]
        performance = (current_price - purchaseprice) * share_no
        total_performance += performance
        print(f"Ticker: {ticker}\n1. Shares: {share_no}\n2. Purchase Price: {purchaseprice}\n3. Current Price: {current_price}\n4. Performance: ${performance:.2f}")
    print(f"\nTotal portfolio performance: ${total_performance}")
    
def menu():
    while True:
        print("\nStock Portfolio Manager\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit\n")
        choice = input("Choose an option: ")
        match choice:
            case '1':
                ticker = input("Enter stock ticker: ").upper()
                no_share = int(input("Enter number of shares: "))
                purchaseprice = float(input("Enter purchase price: "))
                add_stockdata(ticker,no_share,purchaseprice)
                print(f"Successfully added ticker {ticker} data to portfolio.")
            case '2':
                ticker = input("Enter stock ticker to remove: ").upper()
                remove_stockdata(ticker)
                print(f"Successfully removed ticker {ticker} data from portfolio.")
            case '3':
                display_portfolio()
            case '4':
                print("Exiting program.")
                break
            case _:
                print("Unknown choice. Please enter a valid choice.")

if __name__== "__main__":
    menu()

