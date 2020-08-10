### Covid19 Cases Diplay Python By NF Py Developers

#### Join Our Telegram Channel [ProgHub09](http://t.me/ProgHub09) and Also Download Our App.


![Insta Image Here](Covid_Py.jpg)

Python File Code :

```
from covid import Covid

country = input("Enter The Country Name for See Covid-19 Cases : ")

covid = Covid()
cases = covid.get_status_by_country_name(country)
for x in cases:
    print(x, ":" , cases[x])

# Code By NorthFox PyDevelopers
```