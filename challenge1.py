"""
Challenge: Poor Man's Bar Chart.

Author: Jack Ratermann
Date: May 25, 2024
"""
from termcolor import colored

print(colored("\n - Poor Man's Bar Chart - \n", "cyan", attrs=["bold"]))
user_input = input("Please Enter Your Input:\n")
# Example Input: The quick brown fox jumped over the lazy dog.
chart = {
    'a': '',
    'e': '',
    'i': '',
    'o': '',
    'u': '',
}
chart_size = [0, 0, 0, 0, 0]
for i in user_input:
    if i.lower() == 'a':
        chart['a'] += 'a, '
        chart_size[0] += 1
    elif i.lower() == 'e':
        chart['e'] += 'e, '
        chart_size[1] += 1
    elif i.lower() == 'i':
        chart['i'] += 'i, '
        chart_size[2] += 1
    elif i.lower() == 'o':
        chart['o'] += 'o, '
        chart_size[3] += 1
    elif i.lower() == 'u':
        chart['u'] += 'u, '
        chart_size[4] += 1
chart_elements = (chart.get('a'), chart.get('e'), chart.get('i'), chart.get('o'), chart.get('u'))
j = 0
for i in chart_elements:
    if i != '':
        print(colored(i + ": " + str(chart_size[j]), "green"))
    j += 1
print("\n")
print("Thank You For Playing\n")
