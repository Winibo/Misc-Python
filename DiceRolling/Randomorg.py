import mechanize
from bs4 import BeautifulSoup

url = "https://www.random.org/integers/"
num = input("Number of dice(max 10,000):")
minimum = "1"
maximum = input("Maximum(max 1,000,000,000):")
# base, col, formatting, and rnd not used, but are required for url, and appear to have a use in the site
# might actually want to use a different base?
base = "10"
col = "20"
formatting = "html"
rnd = "new"
url = url + "?num=" + num + "&min=" + minimum + "&max=" + maximum + "&col=" + col + "&base=" + base + "&format="\
      + formatting + "&rnd=" + rnd

br = mechanize.Browser()
br.set_handle_robots(False)
open1 = br.open(url)
soup = BeautifulSoup(open1, 'html5lib')
pre = soup.find_all('pre')[-1]
averagestart = pre.text.strip()
average = averagestart.split()
total = 0
print(averagestart)
for x in average:
      total = total + int(x)
print("mean:")
print(total/int(num))
print("Total:")
print(total)
