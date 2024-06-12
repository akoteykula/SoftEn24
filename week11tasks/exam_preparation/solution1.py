from typing import Optional
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re


def task_1():
    import requests
    session = requests.session()
    url = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw"
    response = session.get(url)

    if response.status_code == 200:
        response_data: Optional[dict] = response.json()
        print("Current time: {}:{}:{}".format(
            response_data.get("hour"),
            response_data.get("minute"),
            response_data.get("seconds"),
        ))
    else:
        print("Unable to fetch data. Error: {}".format(response.status_code))


def task_2():
    url = "https://iso.uni.lodz.pl/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\\b\\w+\\b', text.lower())
    word_count = Counter(words)

    if word_count:
        most_common_word, frequency = word_count.most_common(1)[0]
        print(most_common_word, frequency)

def task_3():
    import pandas as pd

    file_path = 'StudentsPerformance.csv'
    df = pd.read_csv(file_path)

    math_median = df['math score'].median()
    reading_median = df['reading score'].median()
    writing_median = df['writing score'].median()

    largest_median = max(math_median, reading_median, writing_median)
    largest_median


def task_4():
    import matplotlib.pyplot as plt

    # Assuming the data is already loaded as df from Task 3

    # Plotting the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['math score'], df['writing score'], alpha=0.5)
    plt.xlabel('Math Score')
    plt.ylabel('Writing Score')
    plt.title('Writing Score vs Math Score')
    plt.show()

