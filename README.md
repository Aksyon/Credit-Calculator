# Credit-Calculator
There is a credit calculator that can calculate annuity payments and
differential payments.

You need to provide the credit info (amount, interest, downpayment, term)
and programm will give you the message with some data: month payment, total
amount of interest for the whole period, total amount of payments.

author: https://github.com/Aksyon / Aleksandr Aksyonov

How to start the program:

1) Import module credit_calculator_module.

2) Create credit calculator object by calling function create_creadit().

3) Input info: amount, interest, downpayment, term). Also input one of the
next comands: ANUIT - for anuity payments calculation and DIFF for differential
payments calculations.

4) Call function main() with the providing before created object.

Example:
```python
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