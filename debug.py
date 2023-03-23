from lib import *

# code here
# e.g.
s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )
fr2 = FundingRound( s1, vc1, 'Pre-Seed', 300000000 )
s2 = Startup( 'Gails Business', 'Gail Hobbs', 'www.studioghobbli.com' )
vc1.offer_contract(s2, 'Pre-Seed', 45000)

vc2 = VentureCapitalist( 'Gail Hobbs', 20000000000 )
vc2.offer_contract(s2, 'Pre-Seed', 700000)
vc2.offer_contract(s1, 'Pre-Seed', 1)


print(vc1.invested('www.pp.com'))
print()
print(vc1.biggest_investment().investment)
print(vc1.portfolio()[0].name)
print()
for fr in vc1.funding_rounds():
    print(fr.investment)

print()
for investor in s2.big_investors():
    print(investor.name, investor.total_worth)

print()
for investor in s1.investors():
    print(investor.name)

print()
print(s2.total_funds())

print()
print(s2.num_funding_rounds())

print()
s2.sign_contract(vc2, 'Pre-Seed', 25)
print(s2.num_funding_rounds())

# do not remove
#import ipdb; ipdb.set_trace()
