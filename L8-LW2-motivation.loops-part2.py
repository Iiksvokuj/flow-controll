# ROBOT
# new - battery

batteryCharge      = 70
consumptionBattery = 10  #%/m

steps              = 0   # m
step               = 1   # m

# 2. ITERATIVE - SIMULATION
# ######## STEP - BEGIN ########
steps = step
batteryCharge = batteryCharge - consumptionBattery
print("STEPS: ", steps, " CHARGE: ", batteryCharge, "%")
# ######## STEP - END   ########

