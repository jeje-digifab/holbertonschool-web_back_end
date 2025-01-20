function displayMessage() {
  console.log('Welcome to Holberton School, what is your name?');

  let input = '';

  process.stdin.on('data', (data) => {
    input += data.toString();
    if (!process.stdin.isTTY) {
      console.log(`Your name is: ${input.trim()}`);
      console.log('This important software is now closing');
      process.exit();
    } else {
      console.log(`Your name is: ${input.trim()}`);
      process.exit();
    }
  });

  if (process.stdin.isTTY) {
    process.stdin.on('end', () => {
      console.log('This important software is now closing');
      process.exit();
    });
  }
}

displayMessage();

module.exports = displayMessage;
