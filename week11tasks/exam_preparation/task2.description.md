The image contains another list of tasks. Here is the content:

**Task 1**

Find the number of words in the following text that start with a capital letter. Use the space as the word separator.

```
If you need to Link to some research from a website or on social media, We want to encourage you to .Link to a RePEc page instead of directly to the full text.
```

Hint: The `s.isupper()` method returns `True` if all the characters in the string `s` are in upper case, otherwise `False`.

**Task 2**

Work with file `phases_soften.html`. It contains the description of four phases of software engineering. Display the title of each phase and the first paragraph after the title. For example, the first phase should be displayed in the following way:

```
Phase 1
This is where the application or software is created. Finding and fixing application security issues in this early stage is far less costly than waiting until after an application has been deployed, so empowering developers to create secure software from inception is critical.
```

- Then choose the title for each phase from the following list: (Deployment, Development, Monitoring, Testing)

Hint: If `element` is an element (found for example with `find()` or `find_all()` methods) then `element.find_next()` returns the next element. The tag name of the next element is optionally specified such that `element.find_next("a")` is the next a-tag and `element.find_next("p")` is the next p-tag.

**Task 3**

Work with file `covid_19_clean.csv`.

1. Find the number of deaths in all countries altogether recorded on June 1 2020.
2. Find the Western Pacific countries (the value of the 'WHO Region' column is 'Western Pacific') such that the number of the confirmed cases (column 'Confirmed') on June 1 2020 is larger than the mean value of the confirmed cases in all countries (without any constraint on the value of the 'WHO Region') on the same day.

**Task 4**

Function `cnst(i:int)` from file `cnst.py` takes a single integer as the input parameter and returns an integer. You are said the output and input integers are the same. Test this statement.

You get 0.5 points in case of a correct test, but you earn 1 point if your test is placed to the file with the opening lines:

```python
import unittest
from cnst import cnst
class TestBuiltins(unittest.TestCase):
```

and the test is called from the command line. In case of Jupyter notebook, `<command>` imitates the command line.

---

Let's proceed with these tasks. Do you have any specific task you want to start with?