from .funding_round import FundingRound

class Startup:
   all = []
   def __init__(self, name, founder, domain):
      self.name = name
      self._founder = founder
      self._domain = domain
      Startup.all.append(founder)


   def get_founder(self):
      return self._founder
   
   def set_founder(self, founder):
      pass

   founder = property(get_founder, set_founder)

   def get_domain(self):
      return self._domain
   
   def set_domain(self,  domain):
      pass

   domain = property(get_domain, set_domain)

   def pivot(self, name, domain):
      self._domain = domain
      self.name = name


   @classmethod
   def find_by_founder(cls, founder):
      for startup in cls.all:
         if (startup.get_founder() == founder):
            return startup
      
      return None
   
   @classmethod
   def domains(cls):
      return [startup.get_domain() for startup in cls.all]
   

   def sign_contract(self, venture_capitalist, type, investment):
      FundingRound(self, venture_capitalist, type, investment)

   def num_funding_rounds(self):
      return len([fr for fr in FundingRound.all if fr.startup == self])

   def total_funds(self):
      return sum([fr.investment for fr in FundingRound.all if fr.startup == self])
   
   def investors(self):
      return list(set([fr.venture_capitalist for fr in FundingRound.all if fr.startup == self]))
   
   def big_investors(self):
      from .venture_capitalist import VentureCapitalist
      return [fr.venture_capitalist for fr in FundingRound.all if fr.startup == self and fr.venture_capitalist in VentureCapitalist.tres_commas_club()]
   