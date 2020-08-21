## Covid19 Cases Diplay Python By NF Py Developers

##### 📫 Connect with me here:<br />
 <br />
 <p>
  <a href="https://www.instagram.com/princu09">
    <img src="https://img.shields.io/badge/princu.09-386938188?style=flat&logo=instagram&color=black">
  </a> &nbsp; 
  <a href="https://twitter.com/princu09">
    <img src="https://img.shields.io/badge/@princu09-30302f?style=flat&logo=twitter&color=black">
  </a>&nbsp; 
  <a href="https://github.com/princu09">
    <img src="https://img.shields.io/badge/@princu09-30302f?style=flat&logo=github&color=black">
  </a>&nbsp;
    <a href="https://www.t.me/proghub09">
    <img src="https://img.shields.io/badge/ProgHub09-386938188?style=flat&logo=telegram&color=black">
  </a>
</p>

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
