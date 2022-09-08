# Credit-Calculator
There is a credit calculator that can calculate annuity payments and
differential payments.

You need to provide the credit info (amount, interest, downpayment, term)
and programm will give you the message with some data: month payment, total
amount of interest for the whole period, total amount of payments.

Levenshtein distance used for validation of input data in the function read_data().

author: https://github.com/Aksyon / Aleksandr Aksyonov

How to start the program:

1) Import module credit_calculator_module.

2) Give a message with info about credit parameters:
```python
message = 'amount: 1000000\ninterest: 5.5\ndownpayment: 20000\ntewm: 7\ncalculator: annuity'
```
There are annuit and differential calculators available (annuit - for anuity payments calculation and differential for differential
payments calculations.

2) Read data from the message by calling function read_data().

3) Call function create_credit() for creating object.

4) Call function main() with the providing created object.

Example:
```python
read_data(message)
credit = create_credit()
main(credit)
```

Copyright [2022] [Aleksandr Aksyonov]
```
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   ```