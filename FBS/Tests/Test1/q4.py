area_of_wall = int(input("Enter area of wall: "))
interior_cost = int(input("Enter Ci: "))
exterior_cost = int(input("enter Ce: "))

cost_interior = 8 * interior_cost * area_of_wall
cost_exterior = 6 * exterior_cost * area_of_wall

totalcost = cost_interior + cost_exterior

print(f"ci and ce are {cost_interior} and {cost_exterior} and totalcost is {totalcost}")