### Tasks Summary for README

#### 0. Executing Basic JavaScript with Node.js
- **File:** `0-console.js`
- **Description:** Create a function `displayMessage` that prints a string argument to STDOUT.
- **Usage:**
  ```bash
  node 0-main.js
  ```
  Output:
  ```
  Hello NodeJS!
  ```

#### 1. Using Process stdin
- **File:** `1-stdin.js`
- **Description:** Create a program that interacts with the user via stdin, displaying messages and capturing input.
- **Usage:**
  ```bash
  node 1-stdin.js
  ```
  Output:
  ```
  Welcome to Holberton School, what is your name?
  Bob
  Your name is: Bob
  ```

#### 2. Reading a File Synchronously with Node.js
- **File:** `2-read_file.js`
- **Description:** Create a function `countStudents` that reads a CSV file synchronously and logs student data.
- **Usage:**
  ```bash
  node 2-main_1.js
  ```
  Output:
  ```
  Number of students: 10
  Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
  Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
  ```

#### 3. Reading a File Asynchronously with Node.js
- **File:** `3-read_file_async.js`
- **Description:** Create a function `countStudents` that reads a CSV file asynchronously and logs student data.
- **Usage:**
  ```bash
  node 3-main_1.js
  ```
  Output:
  ```
  Number of students: 10
  Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
  Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
  ```

#### 4. Create a Small HTTP Server Using Node's HTTP Module
- **File:** `4-http.js`
- **Description:** Create a simple HTTP server that listens on port 1245 and displays a message for any endpoint.
- **Usage:**
  ```bash
  node 4-http.js
  ```
  Output:
  ```
  Hello Holberton School!
  ```

#### 5. Create a More Complex HTTP Server Using Node's HTTP Module
- **File:** `5-http.js`
- **Description:** Create an HTTP server that displays different messages based on the URL path.
- **Usage:**
  ```bash
  node 5-http.js database.csv
  ```
  Output:
  ```
  Hello Holberton School!
  ```
  ```
  This is the list of our students
  Number of students: 10
  Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
  Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
  ```

#### 6. Create a Small HTTP Server Using Express
- **File:** `6-http_express.js`
- **Description:** Create a simple HTTP server using Express that listens on port 1245 and displays a message for the `/` endpoint.
- **Usage:**
  ```bash
  node 6-http_express.js
  ```
  Output:
  ```
  Hello Holberton School!
  ```

#### 7. Create a More Complex HTTP Server Using Express
- **File:** `7-http_express.js`
- **Description:** Create an HTTP server using Express that displays different messages based on the URL path.
- **Usage:**
  ```bash
  node 7-http_express.js database.csv
  ```
  Output:
  ```
  Hello Holberton School!
  ```
  ```
  This is the list of our students
  Number of students: 10
  Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
  Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
  ```

#### 8. Organize a Complex HTTP Server Using Express
- **Directory:** `full_server`
- **Description:** Create a structured Express server with controllers, routes, and utility functions.
- **Files:**
  - `full_server/utils.js`
  - `full_server/controllers/AppController.js`
  - `full_server/controllers/StudentsController.js`
  - `full_server/routes/index.js`
  - `full_server/server.js`
- **Usage:**
  ```bash
  npm run dev
  ```
  Output:
  ```
  Hello Holberton School!
  ```
  ```
  This is the list of our students
  Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
  Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
  ```
  ```
  List: Guillaume, Joseph, Paul, Tommy
  ```

### Repository Information
- **GitHub Repository:** `holbertonschool-web_back_end`
- **Directory:** `Node_JS_basic`
