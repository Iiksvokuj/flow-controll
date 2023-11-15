# INPUT

c_name = input ("Your name?: ")      # c_name - client name
c_adress = input ("Your adress?: ")

c_e_index_0 = int(input ("Before  (kWh): "))
c_e_index_1 = int(input ("Month 1 (kWh): ")) # client elecrtic index 1st month
c_e_index_2 = int(input ("Month 2 (kWh): "))
c_e_index_3 = int(input ("Month 3 (kWh): "))

# CTRL + SHIFT + V(arrow down)
# CTRL + SHIFT + D

ec_price_1kWh = 5   # electric company
# OPERATIONS

c_e_month_1kWh = c_e_index_1 - c_e_index_0
c_e_month_2kWh = c_e_index_2 - c_e_index_1
c_e_month_3kWh = c_e_index_3 - c_e_index_2

c_e_bill_m1 = c_e_month_1kWh * ec_price_1kWh
c_e_bill_m2 = c_e_month_2kWh * ec_price_1kWh
c_e_bill_m3 = c_e_month_3kWh * ec_price_1kWh

c_e_kWh_total = c_e_month_1kWh + c_e_month_2kWh + c_e_month_3kWh
c_e_bill_total = c_e_bill_m1 + c_e_bill_m2 + c_e_bill_m3

k_1 = 100 * c_e_month_1kWh / c_e_kWh_total
k_2 = 100 * c_e_month_2kWh / c_e_kWh_total
k_3 = 100 * c_e_month_3kWh / c_e_kWh_total

# OUTPUT
print("CONSUMPTION")
print("M1:", c_e_month_1kWh, "kWh = ", c_e_bill_m1)
print("M2:", c_e_month_2kWh, "kWh = ", c_e_bill_m2)
print("M3:", c_e_month_3kWh, "kWh = ", c_e_bill_m3)
print("-"*30)
print("Total:", c_e_kWh_total, "kWh = ", c_e_bill_total)
print("USAGE GRAPH")
# print(k_1,k_2,k_3)
print("M1:",k_1, "%", "#" * int(k_1))
print("M2:",k_2, "%", "#" * int(k_2))
print("M3:",k_3, "%", "#" * int(k_3))