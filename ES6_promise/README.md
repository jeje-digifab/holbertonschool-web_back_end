### Tasks Summary for README

This repository contains a series of tasks focused on working with Promises in JavaScript. Each task is designed to reinforce understanding and practical application of Promises. Below is a summary of each task:

1. **Keep every promise you make and only make promises you can keep**
   - **File:** `0-promise.js`
   - **Description:** Return a Promise using the prototype function `getResponseFromAPI()`.
   - **Example Usage:**
     ```javascript
     import getResponseFromAPI from "./0-promise.js";
     const response = getResponseFromAPI();
     console.log(response instanceof Promise); // true
     ```

2. **Don't make a promise...if you know you can't keep it**
   - **File:** `1-promise.js`
   - **Description:** Return a promise based on a boolean parameter. Resolve with a success object or reject with an error message.
   - **Example Usage:**
     ```javascript
     import getFullResponseFromAPI from './1-promise';
     console.log(getFullResponseFromAPI(true)); // Promise { { status: 200, body: 'Success' } }
     console.log(getFullResponseFromAPI(false)); // Promise { <rejected> Error: The fake API is not working currently }
     ```

3. **Catch me if you can!**
   - **File:** `2-then.js`
   - **Description:** Append handlers to a promise to return specific objects on resolution or rejection and log a message.
   - **Example Usage:**
     ```javascript
     import handleResponseFromAPI from "./2-then";
     const promise = Promise.resolve();
     handleResponseFromAPI(promise); // Got a response from the API
     ```

4. **Handle multiple successful promises**
   - **File:** `3-all.js`
   - **Description:** Collectively resolve multiple promises and log the results. Handle errors by logging a specific message.
   - **Example Usage:**
     ```javascript
     import handleProfileSignup from "./3-all";
     handleProfileSignup(); // photo-profile-1 Guillaume Salva
     ```

5. **Simple promise**
   - **File:** `4-user-promise.js`
   - **Description:** Return a resolved promise with an object containing firstName and lastName.
   - **Example Usage:**
     ```javascript
     import signUpUser from "./4-user-promise";
     console.log(signUpUser("Bob", "Dylan")); // Promise { { firstName: 'Bob', lastName: 'Dylan' } }
     ```

6. **Reject the promises**
   - **File:** `5-photo-reject.js`
   - **Description:** Return a rejected promise with an error message indicating the file cannot be processed.
   - **Example Usage:**
     ```javascript
     import uploadPhoto from './5-photo-reject';
     console.log(uploadPhoto('guillaume.jpg')); // Promise { <rejected> Error: guillaume.jpg cannot be processed }
     ```

7. **Handle multiple promises**
   - **File:** `6-final-user.js`
   - **Description:** Handle multiple promises and return an array with the status and value/error of each promise.
   - **Example Usage:**
     ```javascript
     import handleProfileSignup from './6-final-user';
     console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg")); // Promise { <pending> }
     ```

8. **Load balancer**
   - **File:** `7-load_balancer.js`
   - **Description:** Return the value of the first resolved promise between two given promises.
   - **Example Usage:**
     ```javascript
     import loadBalancer from "./7-load_balancer";
     const promiseUK = new Promise(resolve => setTimeout(resolve, 100, 'Downloading from UK is faster'));
     const promiseFR = new Promise(resolve => setTimeout(resolve, 200, 'Downloading from FR is faster'));
     console.log(await loadBalancer(promiseUK, promiseFR)); // Downloading from UK is faster
     ```

9. **Throw an error**
   - **File:** `8-try.js`
   - **Description:** Throw an error if the denominator is zero, otherwise return the result of the division.
   - **Example Usage:**
     ```javascript
     import divideFunction from './8-try';
     console.log(divideFunction(10, 2)); // 5
     console.log(divideFunction(10, 0)); // Error: cannot divide by 0
     ```

10. **Throw error / try catch**
    - **File:** `9-try.js`
    - **Description:** Execute a function and append the result or error message to a queue, along with a processing message.
    - **Example Usage:**
      ```javascript
      import guardrail from './9-try';
      import divideFunction from './8-try';
      console.log(guardrail(() => { return divideFunction(10, 2)})); // [ 5, 'Guardrail was processed' ]
      console.log(guardrail(() => { return divideFunction(10, 0)})); // [ 'Error: cannot divide by 0', 'Guardrail was processed' ]
      ```

### Repository Details
- **GitHub Repository:** `holbertonschool-web_back_end`
- **Directory:** `ES6_promise`
