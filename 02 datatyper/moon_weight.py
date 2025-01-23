moon = "Moon"

earth_gravity = 9.807
moon_gravity = 1.622

# my_earth_weight = 85
my_earth_weight = input("Type in your weigth:")
my_earth_weight_number = float(my_earth_weight)

# weight / earth_grav * moon_grav
my_moon_weigth = my_earth_weight_number / earth_gravity * moon_gravity

print (f"my weight on the {moon} is {my_moon_weigth}")
