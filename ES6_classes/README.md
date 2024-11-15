### Task Summary for README

This project involves implementing various ES6 classes and methods in JavaScript. Below is a summary of the tasks:

1. **ClassRoom Class**
   - Implement a class named `ClassRoom` with an attribute `maxStudentsSize`.
   - File: `0-classroom.js`

2. **Initialize Rooms**
   - Import the `ClassRoom` class and implement a function `initializeRooms` that returns an array of 3 `ClassRoom` objects with sizes 19, 20, and 34.
   - File: `1-make_classrooms.js`

3. **HolbertonCourse Class**
   - Implement a class named `HolbertonCourse` with attributes `name`, `length`, and `students`.
   - Include getters and setters for each attribute.
   - File: `2-hbtn_course.js`

4. **Currency Class**
   - Implement a class named `Currency` with attributes `code` and `name`.
   - Include getters and setters for each attribute.
   - Implement a method `displayFullCurrency` to return the attributes in the format `name (code)`.
   - File: `3-currency.js`

5. **Pricing Class**
   - Import the `Currency` class and implement a class named `Pricing` with attributes `amount` and `currency`.
   - Include getters and setters for each attribute.
   - Implement a method `displayFullPrice` to return the attributes in the format `amount currency_name (currency_code)`.
   - Implement a static method `convertPrice` to return the amount multiplied by the conversion rate.
   - File: `4-pricing.js`

6. **Building Class**
   - Implement a class named `Building` with an attribute `sqft`.
   - Consider this class as abstract and ensure any extending class implements `evacuationWarningMessage`.
   - File: `5-building.js`

7. **SkyHighBuilding Class**
   - Extend the `Building` class to create a `SkyHighBuilding` class with additional attribute `floors`.
   - Override the `evacuationWarningMessage` method.
   - File: `6-sky_high.js`

8. **Airport Class**
   - Implement a class named `Airport` with attributes `name` and `code`.
   - Override the default string description to return the airport code.
   - File: `7-airport.js`

9. **HolbertonClass Class**
   - Implement a class named `HolbertonClass` with attributes `size` and `location`.
   - When cast to a Number, return the size.
   - When cast to a String, return the location.
   - File: `8-hbtn_class.js`

10. **Hoisting Fix**
    - Fix the provided code to ensure proper hoisting and functionality.
    - File: `9-hoisting.js`

11. **Car Class**
    - Implement a class named `Car` with attributes `brand`, `motor`, and `color`.
    - Add a method `cloneCar` to return a new object of the class.
    - File: `10-car.js`

### Repository Details
- **GitHub Repository**: `holbertonschool-web_back_end`
- **Directory**: `ES6_classes`

Each task has specific requirements and test cases to ensure proper implementation. The project aims to practice ES6 classes, inheritance, and various JavaScript features.
