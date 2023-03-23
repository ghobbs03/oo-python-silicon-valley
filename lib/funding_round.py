class FundingRound:
    all = []
    def __init__(self, startup, venture_capitalist, type, investment):
        self.startup  = startup
        self.venture_capitalist = venture_capitalist
        self.type = type
        self.investment = investment
        FundingRound.all.append(self)