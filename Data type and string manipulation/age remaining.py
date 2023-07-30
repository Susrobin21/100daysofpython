#age remaining
age = input("What is your current age? ")
age_inint = int(age)
years = 80 - age_inint
months = years*12
weeks = years*52
days = years*365
print(f'you have {years} years, {months} months, {weeks} weeks, {days} days remaining')