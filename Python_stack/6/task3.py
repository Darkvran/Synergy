"""
input: A fishermen, B boats, C weightload, D seats in the boat" 
Output: Count of boats to transfer fishermen
"""
import math
class OutOfRange(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} is out of range"

class InvalidWeight(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"{self.value} is greater than boat mass. Transfer is impossible."

def boats_num(boat_mass:int, fisherman_weights:list[int]):
    boat_num = 0
    fisherman_weights.sort()
    lightweightest = 0
    heavyweightest = len(fisherman_weights) - 1
    while lightweightest <= heavyweightest:
        if fisherman_weights[lightweightest] + fisherman_weights[heavyweightest] <= boat_mass:
            boat_num += 1
            lightweightest += 1
            heavyweightest -= 1
        else:
            boat_num += 1
            heavyweightest -= 1
    return boat_num

boat_mass = int(input("Weight in one boat: "))
if boat_mass > 10e6 or boat_mass < 1:
    raise OutOfRange(boat_mass)

fisherman_count = int(input("How many fishermen need to transfer?"))
if fisherman_count > 100 or fisherman_count < 1:
    raise OutOfRange(fisherman_count)
fisherman_weights = []
for i in range (fisherman_count):
    fisherman_weight = int(input(f"Enter the weight of №{i+1} fisherman: "))
    if fisherman_weight <= boat_mass:
        fisherman_weights.append(fisherman_weight)
    else:
        raise InvalidWeight(fisherman_weight)


print(boats_num(boat_mass, fisherman_weights))
