import MetaTrader5 as mt5

print("🔄 Attempting to connect to MetaTrader 5...")

# Initialize connection to the MT5 terminal
if not mt5.initialize():
    print(f"❌ Failed to connect to MT5. Error code: {mt5.last_error()}")
else:
    print("✅ SUCCESS: Python is connected to MetaTrader 5!")
    
    # Print out your Symphonix account info to confirm identity
    account_info = mt5.account_info()
    if account_info is not None:
        print(f"💳 Account Number: {account_info.login}")
        print(f"🏦 Broker/Server:  {account_info.server}")
        print(f"💰 Balance:        ${account_info.balance:,.2f}")
    else:
        print("⚠️ Connected to terminal, but couldn't retrieve account info details.")
        
    # Always shut down the connection cleanly when done testing
    mt5.shutdown()
    