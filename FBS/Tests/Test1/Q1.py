length = int(input("Enter length:"))
breadth = int(input("Enter Breadth:"))
radius = int(input("Enter Radius:"))

area_of_reactangle = length * breadth
area_of_semicircle = 3.14 * radius * radius / 2

total_area = area_of_reactangle + area_of_semicircle

peri_rect = 2*(length * breadth)
peri_semi = 3.14 * radius + 2 * radius

total_peri = peri_rect + peri_semi

print(f"Total Area and Total Perimeter of figure is {total_area} and {total_peri} Respectively")