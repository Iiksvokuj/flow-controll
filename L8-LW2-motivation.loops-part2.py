# ROBOT
# new - battery

batteryCharge      = 70
consumptionRate = 10  #%/m

steps              = 0   # m
step               = 1   # m

# 2. ITERATIVE - SIMULATION
# ######## STEP - BEGIN ########
steps          +=  step
batteryCharge  -=  consumptionRate
print("STEPS: ", steps, " CHARGE: ", batteryCharge, "%")
# ######## STEP - END   ########

