### Tasks Summary

This repository contains a series of tasks aimed at practicing and understanding various ES6 features in JavaScript. Each task is located in the `ES6_basic` directory of the `holbertonschool-web_back_end` GitHub repository. Below is a summary of each task:

#### 0. Const or let?
- **Task**: Modify the functions `taskFirst` and `taskNext` to use `const` and `let` respectively.
- **Files**: `0-constants.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 0-main.js
  I prefer const when I can. But sometimes let is okay
  ```

#### 1. Block Scope
- **Task**: Modify the variables inside the function `taskBlock` to avoid overwriting within the conditional block.
- **Files**: `1-block-scoped.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 1-main.js
  [ false, true ]
  [ false, true ]
  ```

#### 2. Arrow functions
- **Task**: Rewrite the standard function to use ES6’s arrow syntax.
- **Files**: `2-arrow.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 2-main.js
  [ 'SOMA', 'Union Square', 'Noe Valley' ]
  ```

#### 3. Parameter defaults
- **Task**: Condense the function `getSumOfHoods` to use default parameter values.
- **Files**: `3-default-parameter.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 3-main.js
  142
  56
  41
  ```

#### 4. Rest parameter syntax for functions
- **Task**: Modify the function to return the number of arguments passed using the rest parameter syntax.
- **Files**: `4-rest-parameter.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 4-main.js
  1
  4
  ```

#### 5. The wonders of spread syntax
- **Task**: Use spread syntax to concatenate two arrays and each character of a string.
- **Files**: `5-spread-operator.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 5-main.js
  [ 'a', 'b', 'c', 'd', 'H', 'e', 'l', 'l', 'o' ]
  ```

#### 6. Take advantage of template literals
- **Task**: Rewrite the return statement to use a template literal.
- **Files**: `6-string-interpolation.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 6-main.js
  As of 2017, it was the seventh-highest income county in the United States, with a per capita personal income of $119,868. As of 2015, San Francisco proper had a GDP of $154.2 billion, and a GDP per capita of $178,479.
  ```

#### 7. Object property value shorthand syntax
- **Task**: Modify the `budget` object to use the object property value shorthand syntax.
- **Files**: `7-getBudgetObject.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 7-main.js
  { income: 400, gdp: 700, capita: 900 }
  ```

#### 8. No need to create empty objects before adding in properties
- **Task**: Rewrite the function to use ES6 computed property names on the `budget` object.
- **Files**: `8-getBudgetCurrentYear.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 8-main.js
  { 'income-2021': 2100, 'gdp-2021': 5200, 'capita-2021': 1090 }
  ```

#### 9. ES6 method properties
- **Task**: Rewrite `getFullBudgetObject` to use ES6 method properties in the `fullBudget` object.
- **Files**: `9-getFullBudget.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 9-main.js
  $20
  20 euros
  ```

#### 10. For...of Loops
- **Task**: Rewrite the function `appendToEachArrayValue` to use ES6’s `for...of` operator.
- **Files**: `10-loops.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 10-main.js
  [ 'correctly-appended', 'correctly-fixed', 'correctly-displayed' ]
  ```

#### 11. Iterator
- **Task**: Write a function `createEmployeesObject` that returns an object with the department name and employees.
- **Files**: `11-createEmployeesObject.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 11-main.js
  { Software: [ 'Bob', 'Sylvie' ] }
  ```

#### 12. Let's create a report object
- **Task**: Write a function `createReportObject` that returns an object containing the key `allEmployees` and a method property `getNumberOfDepartments`.
- **Files**: `12-createReportObject.js`
- **Execution Example**:
  ```bash
  bob@dylan:~$ npm run dev 12-main.js
  { engineering: [ 'Bob', 'Jane' ], marketing: [ 'Sylvie' ] }
  2
  ```

This summary provides an overview of the tasks and their corresponding files, along with execution examples for each task.