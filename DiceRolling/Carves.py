import mechanize
from bs4 import BeautifulSoup
import collections
url = "https://www.random.org/integers/"
dice = input("xdx: ")
num, maximum = dice.split("d")
minimum = "1"
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
groups = collections.Counter(average)
print(dict(groups))
input("Press any key to exit")
