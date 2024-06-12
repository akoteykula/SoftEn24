def task1():
    text = "If you need to Link to some research from a website or on social media, We want to encourage you to .Link to a RePEc page instead of directly to the full text."
    words = text.split()
    capital_words = [word for word in words if word[0].isupper()]
    num_capital_words = len(capital_words)
    print(num_capital_words)


def task2():
    from bs4 import BeautifulSoup

    # Load the HTML content
    with open("phases_soften.html", "r") as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")
    phases = ["Deployment", "Development", "Monitoring", "Testing"]

    for phase in phases:
        title = soup.find("h2", text=phase)
        if title:
            paragraph = title.find_next("p").text
            print(f"{phase}\n{paragraph}\n")

def task3():
    import pandas as pd

    # Load the CSV file
    df = pd.read_csv("covid_19_clean.csv")

    # Task 3.1: Find the number of deaths in all countries altogether recorded on June 1 2020.
    june_1_data = df[df['Date'] == '2020-06-01']
    total_deaths_june_1 = june_1_data['Deaths'].sum()
    total_deaths_june_1

    # Task 3.2: Find the Western Pacific countries with confirmed cases larger than the mean value.
    western_pacific = june_1_data[june_1_data['WHO Region'] == 'Western Pacific']
    mean_confirmed = june_1_data['Confirmed'].mean()
    high_confirmed_western_pacific = western_pacific[western_pacific['Confirmed'] > mean_confirmed]
    high_confirmed_western_pacific_countries = high_confirmed_western_pacific['Country'].tolist()
    print(high_confirmed_western_pacific_countries)


import unittest
from cnst import cnst

class TestBuiltins(unittest.TestCase):
    def test_cnst(self):
        for i in range(-100, 100):
            self.assertEqual(cnst(i), i)


if __name__ == '__main__':
    unittest.main()

task1()