start_year = int(input("Enter stating year: "))
end_year = int(input("Enter ending year: "))
leap_year = []
for year in range(start_year, end_year):
    if year % 400 == 0 and year % 100 == 0:
        leap_year.append(year)
    elif year % 4 == 0 and year % 100 != 0:
        leap_year.append(year)
print(leap_year)
