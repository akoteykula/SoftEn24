# Software Engineering Exam

### First Version

### Task 1:

To find the temperature on 2023-05-23 at 23:00 using the Open Meteo API Archive, we need to make a request to the API with the appropriate parameters.

### Solution:

1. Use the requests library to fetch the data from the API.
2. Parse the JSON response to find the temperature at the specified time.

```python
import requests

url = "<https://archive-api.open-meteo.com/v1/archive>"
params = {
    "latitude": 51.77,
    "longitude": 19.47,
    "start_date": "2023-05-13",
    "end_date": "2023-05-27",
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params)
data = response.json()

# Extracting the temperature at 2023-05-23 23:00
date_time = "2023-05-23T23:00"
temperature = None

for i, time in enumerate(data['hourly']['time']):
    if time == date_time:
        temperature = data['hourly']['temperature_2m'][i]
        break

temperature

```

### Task 2:

To extract and print the Hourly Weather Variables from the Open Meteo API Documentation, we need to fetch the relevant information from the documentation page.

### Solution:

1. Parse the documentation page to find the Hourly Weather Variables.
2. Print the variables and their count.

```python
import requests
from bs4 import BeautifulSoup

url = "<https://open-meteo.com/en/docs/historical-weather-api>"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting Hourly Weather Variables from the documentation
variables_section = soup.find('section', {'id': 'hourly-weather-variables'})
variables_list = variables_section.find_all('li')

variables = [var.text for var in variables_list]
variables_count = len(variables)

variables, variables_count

```

### Task 3:

Using the file `covid_19_clean.csv`, we need to find:

- The number of days with positive records of active cases in Poland.
- The date when the maximal number of active cases is attained.

### Solution:

1. Load the CSV file into a DataFrame.
2. Filter the records for Poland and find the required information.

```python
import pandas as pd

# Assuming the CSV file is uploaded to the working directory
file_path = 'covid_19_clean.csv'
df = pd.read_csv(file_path)

# Filtering data for Poland
poland_data = df[df['Country/Region'] == 'Poland']

# Finding the number of days with positive active cases
positive_active_cases_days = poland_data[poland_data['Active'] > 0].shape[0]

# Finding the date(s) with the maximal number of active cases
max_active_cases = poland_data['Active'].max()
max_active_cases_dates = poland_data[poland_data['Active'] == max_active_cases]['Date']

positive_active_cases_days, max_active_cases_dates.tolist()

```

### Task 4:

Plot the number of active cases in Poland using matplotlib.

### Solution:

1. Load the data as in Task 3.
2. Plot the data using matplotlib.

```python
import matplotlib.pyplot as plt

# Assuming the data is already loaded as poland_data from Task 3

# Plotting the number of active cases
plt.figure(figsize=(10, 6))
plt.plot(poland_data['Date'], poland_data['Active'], label='Active Cases')
plt.xlabel('Date')
plt.ylabel('Number of Active Cases')
plt.title('Number of Active Cases in Poland')
plt.xticks(rotation=45)
plt.legend()
plt.show()

```

### Task 5:

Create a separate test file for the identity function and set up unit tests.

### Solution:

1. Create two files: `identity.py` and `test_identity.py`.
2. In `identity.py`, define the function.
3. In `test_identity.py`, write the unit tests.

[**identity.py**](http://identity.py/)

```python
import numpy as np
import math

def identity(x=1):
    z = complex(0, 1)
    return math.atan2(z.imag, z.real) / (2 * np.pi) * 4 * x

```

**test_identity.py**

```python
import unittest
from identity import identity

class TestIdentityFunction(unittest.TestCase):

    def test_identity_default(self):
        self.assertEqual(identity(), 1)

    def test_identity_with_zero(self):
        self.assertEqual(identity(0), 0)

    def test_identity_with_positive(self):
        self.assertEqual(identity(5), 5)

    def test_identity_with_negative(self):
        self.assertEqual(identity(-3), -3)

    def test_identity_with_fraction(self):
        self.assertEqual(identity(2.5), 2.5)

if __name__ == '__main__':
    unittest.main()
```

To run the tests from the terminal:

```
python -m unittest test_identity.py
```

To run the tests from a Jupyter notebook cell:

```python
!python -m unittest test_identity.py
```

These solutions cover the tasks you outlined. You can run and test each part accordingly.

### Second Version

### Task 1:

To find the current time in Warsaw using the provided Time API, we need to make a request to the API and parse the JSON response to get the current time.

### Solution:

```python
import requests

url = "<https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw>"
response = requests.get(url)
data = response.json()

current_time = data['dateTime']
current_time

```

### Task 2:

To find the most frequent word on the ISO University of Lodz page, we need to fetch the page content, parse it, and count the frequency of each word.

### Solution:

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

url = "<https://iso.uni.lodz.pl/>"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract text from the page
text = soup.get_text()

# Remove special characters and split the text into words
words = re.findall(r'\\b\\w+\\b', text.lower())

# Count the frequency of each word
word_count = Counter(words)
most_common_word, frequency = word_count.most_common(1)[0]

most_common_word, frequency

```

### Task 3:

Using the file `StudentsPerformance.csv`, determine the largest median among results in 'math score', 'reading score', and 'writing score'.

### Solution:

1. Load the CSV file into a DataFrame.
2. Calculate the median for each score column.
3. Find the largest median.

```python
import pandas as pd

# Load the CSV file
file_path = 'StudentsPerformance.csv'
df = pd.read_csv(file_path)

# Calculate the median for each score
math_median = df['math score'].median()
reading_median = df['reading score'].median()
writing_median = df['writing score'].median()

# Find the largest median
largest_median = max(math_median, reading_median, writing_median)
largest_median

```

### Task 4:

Using the file `StudentsPerformance.csv`, make a scatter plot of 'writing score' vs 'math score'. Label the axes.

### Solution:

1. Load the data as in Task 3.
2. Plot the data using matplotlib.

```python
import matplotlib.pyplot as plt

# Assuming the data is already loaded as df from Task 3

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['math score'], df['writing score'], alpha=0.5)
plt.xlabel('Math Score')
plt.ylabel('Writing Score')
plt.title('Writing Score vs Math Score')
plt.show()

```

These solutions should address the tasks you outlined. Each part can be run and tested accordingly.

### In class assignment

### Task 1: Fetch current time in Warsaw using the given API.

To achieve this, we'll need to use the `requests` library to make an API call.

```python
import requests

def get_current_time_in_warsaw():
    url = "<https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw>"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['dateTime']
    else:
        return None

current_time = get_current_time_in_warsaw()
print("Current time in Warsaw:", current_time)

```

### Task 2: Extract prices of apartments from a webpage and find the lowest and highest prices

Since we don't have a specific URL for the apartment listings, I'll outline the general approach to achieve this using BeautifulSoup.

```python
import requests
from bs4 import BeautifulSoup

def get_apartment_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    prices = []

    # Assuming prices are within elements with class name 'price'
    for price_tag in soup.find_all(class_='price'):
        price = price_tag.get_text().strip()
        price = int(price.replace('$', '').replace(',', ''))  # Assuming prices are in the format $1,000, etc.
        prices.append(price)

    return prices

# Example URL (replace with actual URL)
url = "<http://example.com/apartments>"
prices = get_apartment_prices(url)
print(f"Number of ads: {len(prices)}")
print(f"Lowest price: ${min(prices)}")
print(f"Highest price: ${max(prices)}")

```

### Task 3: Analyze students' performance in exams

Let's load the CSV file and perform the required analysis using pandas.

```python
import pandas as pd

# 1.1 Read the data from the CSV file
file_path = '/mnt/data/StudentsPerformance.csv'
data = pd.read_csv(file_path)

# 1.2 Check the descriptive statistics and find the subject with the greatest mean score
descriptive_stats = data.describe()
mean_scores = descriptive_stats.loc['mean', ['math score', 'reading score', 'writing score']]
greatest_mean_subject = mean_scores.idxmax()

# 1.3 Check for missing values and remove rows with missing values
missing_values = data.isnull().sum()
clean_data = data.dropna()

# 1.4 Filter the data for students with bachelor's degree and math scores above the median
median_math_score = clean_data['math score'].median()
filtered_data = clean_data[(clean_data['parental level of education'] == "bachelor's degree") & (clean_data['math score'] > median_math_score)]

# 1.5 Calculate the ratio of females and males in the dataset
gender_ratio = clean_data['gender'].value_counts(normalize=True)

# 1.6 Check the representation of races/ethnicities
race_ethnicity_counts = clean_data['race/ethnicity'].value_counts()

import ace_tools as tools; tools.display_dataframe_to_user(name="Descriptive Statistics", dataframe=descriptive_stats)

print(f"Subject with greatest mean score: {greatest_mean_subject}")
print(f"Missing values in the dataset: \\n{missing_values}")
print(f"Gender ratio (female:male): {gender_ratio['female']}:{gender_ratio['male']}")
print("Race/Ethnicity counts: \\n", race_ethnicity_counts)

```

### Task 4: Create and run unit tests

1. Create the `test_tmp.py` file:

```python
import unittest

class TestBuiltins(unittest.TestCase):
    """Test some python built-in methods"""
    def test_len(self):
        self.assertEqual(5, len("hello"))
        self.assertEqual(3, len(['a','b','c']))
        # edge case
        self.assertEqual(0, len(""))

    def test_str_upper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("ABc".isupper())
        s = ""  # edge case
        self.assertFalse(s.isupper())

if __name__ == '__main__':
    unittest.main()

```

1. Modify the file to run with `python -m`:

```python
if __name__ == '__main__':
    unittest.main(module=__name__, verbosity=2)

```

1. Add tests that fail:

```python
import unittest

class TestBuiltins(unittest.TestCase):
    """Test some python built-in methods"""
    def test_len(self):
        self.assertEqual(5, len("hello"))
        self.assertEqual(3, len(['a','b','c']))
        # edge case
        self.assertEqual(0, len(""))

    def test_str_upper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("ABc".isupper())
        s = ""  # edge case
        self.assertFalse(s.isupper())

    def test_fail_case_1(self):
        self.assertEqual(2, 3)

    def test_fail_case_2(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main(module=__name__, verbosity=2)

```

The `-v` flag increases the verbosity of the output.

### Task 5: Function to prompt user for positive integer

```python
def get_positive_integer():
    while True:
        try:
            user_input = int(input("Enter a positive integer: "))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Unit test with mock input
import unittest
from unittest.mock import patch

class TestPositiveIntegerInput(unittest.TestCase):
    @patch('builtins.input', return_value='2')
    def test_get_positive_integer(self, mock_input):
        self.assertEqual(get_positive_integer(), 2)

if __name__ == '__main__':
    unittest.main(module=__name__, verbosity=2)

```

You can save this test in a file and run it with `python -m testfilename`.

Let me know if you need any specific part implemented or further details!