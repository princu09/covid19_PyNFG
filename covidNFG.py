from covid import Covid

country = input("Enter The Country Name for See Covid-19 Cases : ")

covid = Covid()
cases = covid.get_status_by_country_name(country)
for x in cases:
    print(x, ":" , cases[x])

# Code By NorthFox PyDevelopers