basic = float(input("Enter basic salary: "))

hra = basic * 20 / 100
da = basic * 10 / 100
net_salary = basic + hra + da

print("\nSalary Breakdown")
print(f"Basic Salary: Rs. {basic:.2f}")
print(f"HRA (20%): Rs. {hra:.2f}")
print(f"DA (10%): Rs. {da:.2f}")
print(f"Net Salary: Rs. {net_salary:.2f}")
