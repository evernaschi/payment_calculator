
# Payment Calculator

This is a tool for calculating the total that the company has to pay an employee, based on the hours they worked and the times during which they worked.

- Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.  
- Output: indicate how much the employee has to be paid  

\
\
The following abbreviations will be used for entering data:

**MO**: Monday

**TU**: Tuesday

**WE**: Wednesday

**TH**: Thursday

**FR**: Friday

**SA**: Saturday

**SU**: Sunday  
\
\
For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

## Setup

1. Install [`Python`][python_setup].

1. Clone this repository:

    ```
    git clone https://github.com/evernaschi/payment_calculator.git
    ```

## How to run

1. Set the input file (input.txt) according to the input format
 
1. Run the program:

    ```
    python main.py
    ```

1. You will see the output with the calculated payment printed in the terminal

## Testing:
If you want to try the testing tools for this program follow these steps:
1. Install [`Pip`][pip_setup].
2. Install [`Pytest`][pytest_setup]:
    ```
    pip install -U pytest
    ```
3. Run the tests in the project directory
    ```
    pytest
    ```

[python_setup]: https://www.python.org/downloads/
[pip_setup]: https://pypi.org/project/pip/
[pytest_setup]:https://docs.pytest.org/en/7.1.x/
