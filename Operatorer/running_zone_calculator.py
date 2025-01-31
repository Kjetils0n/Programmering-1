print("====Calculator your running zones based on average heartrate====")

# getting the heartrate numbers from the user, that we need for out calculations
average_5k_heartrate = input("Type inn your average heartrate from your 5k runs: ")
average_5k_heartrate = float(average_5k_heartrate)
average_10k_heartrate = float(input("Type inn your average heartrate from your 10k runs: "))

# Take away the given number for the distance, to get the lactate threshold
average_5k_heartrate -= 15
average_10k_heartrate -= 10


# the formula for the mean lactate threshold /
lactate_threshold = (average_5k_heartrate + average_10k_heartrate) / 2

print (f"Your calculated lactate threshold is {lactate_threshold}")

# calculation the different heartrate zones
# The zones are in different percentages of the lactate threshold
zone1 = int(lactate_threshold * 0.8)
zone2_from = int(lactate_threshold * 0.81)
zone2_to = int(lactate_threshold * 0.89)
zone3_from = int(lactate_threshold * 0.90)
zone3_to = int(lactate_threshold * 0.95)
zone4_from = int(lactate_threshold * 0.96)
zone4_to = int(lactate_threshold * 0.99)
zone5 = int(lactate_threshold)

# Printing the zones to the user
print ("\n==========ZONES==========")
print(f"Your zone 1 is up to heartrate of {zone1}")
print(f"Your zone 2 heartrate from {zone2_from} to {zone2_to}")
print(f"Your zone 3 heartrate from {zone3_from} to {zone3_to}")
print(f"Your zone 4 heartrate from {zone4_from} to {zone4_to}")
print(f"Your zone 5 heartrate above {zone5}")
