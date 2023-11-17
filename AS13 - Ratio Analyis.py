# Create a program to calculate common Ratio Analyses

def calc_gpm(gp, s):
    gpm = (gp / s) * 100
    return gpm

def calc_npm(np, s):
    npm = (np / s) * 100
    return npm

gon = input("If you would like to calculate gross profit margin, enter 'gpm'\t"
            "If you would like to calculate net profit margin, enter 'npm':\n")

if gon == "gpm":
    gross_profit = float(input("Enter this season's gross profit: "))
    sales = int(input("Enter this season's sale: "))
    print(f"The gross profit this season is {calc_gpm(gross_profit, sales)}%")
elif gon == "npm":
    net_profit = float(input("Enter this season's net profit: "))
    sales = int(input("Enter this season's sale: "))
    print(f"The net profit this season is {calc_npm(net_profit, sales)}%")
else:
    print("Not an option")