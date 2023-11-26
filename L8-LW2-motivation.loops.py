# ROBOT
# new - battery

batteryCharge      = 70
consumptionBattery = 10  #%/m

# CALCULATE HOW MANY METERS/STEPS?
# 1. SIMPLE

estimatedDistance = batteryCharge / consumptionBattery
print("Estmated Distance: ", estimatedDistance, "m")