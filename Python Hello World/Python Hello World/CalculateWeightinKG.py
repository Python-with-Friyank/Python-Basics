userName = input("Please type me your Name ")
print("Hello "+ userName +",")
weightinPounds = input(userName+ " Please type in your Weight(Pounds) ")
weightinKG = float(weightinPounds)  * 0.45359237
print(userName + ' Your Weight is ' + str(weightinKG) + "(Kilogram)")