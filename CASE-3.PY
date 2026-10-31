basic = float(input("Basic pay: "))
hours = float(input("Overtime hours: "))
hra = basic * 0.20
da = basic * 0.10
gross = basic + hra + da + hours * 150
if gross <= 30000:
    net = gross * 0.95
else:
    net = gross * 0.90
print("Gross salary:", gross)
print("Net salary:", net)
