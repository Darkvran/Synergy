"""
Two investors, Mike and Ivan, want to invest in a startup.
The founders have set a minimum investment requirement of X dollars.
There is no upper limit on the investment amount.

Mike has A dollars, and Ivan has B dollars.

Determine the outcome based on their individual and combined capital:

Output 2 if both can invest individually.

Output Mike if only Mike has enough money.
Output Ivan if only Ivan has enough money.

Output 1 if neither can invest alone, 
but their combined capital is enough to meet the minimum requirement.

Output 0 if they cannot afford to invest even together.
"""

class Investor:
    """
    The investor class
    """
    def __init__(self, name:str, capital:float):
        self.name: str = name
        self.capital = capital

class NotTwoInvestors(Exception):
    """
    Exception when the len of list of investors list is not 2
    """
    def __init__(self, investors: list[Investor]):
        self.investors:list[Investor] = investors

    def __str__(self):
        return f"There are not two investors in {self.investors}"

class Startup:
    """
    Class for startup
    """
    def __init__(self, minSumToInvest:float, investors: list[Investor]):
        self.minSumToInvest: float = minSumToInvest
        self.investors:list[Investor] = investors

    def find_suit_investors(self):
        """
        Calculate suitable investors from self.investors
        """
        suit_investors = []
        cost_investors = 0
        for investor in self.investors:
            if investor.capital >= self.minSumToInvest:
                suit_investors.append(investor.name)
            cost_investors += investor.capital
        if len(suit_investors) == 1:
            return suit_investors[0]
        elif len(suit_investors) == 2:
            return 2
        elif len(suit_investors) == 0 and cost_investors >= self.minSumToInvest:
            return 1
        else:
            return 0

startup = Startup(100, [Investor("Mike", 80), Investor("Ivan", 20)])
print(startup.find_suit_investors())
