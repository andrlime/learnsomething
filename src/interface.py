class ProcrcastinationExchange:
    # implement this!
    # later
    balance = 0
    trades_to_do_later = []

    def __init__(self, initialBalance):
        """Initial Balance is the amount that each account should start with."""
        self.balance = initialBalance
        self.trades_to_do_later = []

    def add_trade(self, trade):
        """Adds a trade to the exchange (validation required)
        and returns a match if required. It is up to you on how you will
        handle representing trades. """
        self.trades_to_do_later.append(trade)

