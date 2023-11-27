# ROBOT
# new - battery

batteryCharge      = 70
consumptionRate = 10  #%/m

steps              = 0   # m
step               = 1   # m

# DRY - Don't Repeat Yourself
# 2. ITERATIVE - SIMULATION
while True:
    # ######## STEP - BEGIN ########
    steps          +=  step
    batteryCharge  -=  consumptionRate
    print("STEPS: ", steps, " CHARGE: ", batteryCharge, "%")
    if batteryCharge <= 10:
        print("WARNING!!! Need to charge")
    # ######## STEP - END   ########

