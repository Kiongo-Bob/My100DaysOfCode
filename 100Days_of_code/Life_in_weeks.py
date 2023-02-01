# Use loops to calculate time left precisely
current_age_years = int(input("Enter your age in years only: "))
# current_age_months = int(input("Enter the months: "))
# current_age_weeks = int(input("Enter your age in weeks: "))
# current_age_days = int(input("Enter your age in days: "))

years_left = (90 -current_age_years) 
months_left = years_left *12
weeks_left = (years_left * 52)
days_left = (years_left) * 365
if months_left == 0 or weeks_left == 0:
    print("It is time to translate!")
else:
    print(f"You have {months_left} months or {weeks_left} weeks or {days_left} days to live!")