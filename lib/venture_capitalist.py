from .funding_round import FundingRound

class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)


    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls.all if vc.total_worth >= 1000000000]

    def offer_contract(self, startup, type, investment):
        FundingRound(startup, self, type, investment)

    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]
    
    def portfolio(self):
        return list(set([fr.startup for fr in FundingRound.all if fr.venture_capitalist == self]))
    
    def biggest_investment(self):
        frs = [fr for fr in FundingRound.all if fr.venture_capitalist == self]
        
        investments = dict()
        for fr in frs:
            investments[fr] = fr.investment
            
        return max(investments, key=investments.get)

        


    
    def invested(self, domain):
        return sum([fr.investment for fr in FundingRound.all if fr.venture_capitalist == self])