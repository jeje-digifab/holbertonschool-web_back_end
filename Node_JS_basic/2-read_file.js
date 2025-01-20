const fs = require('fs');
const readline = require('readline');

function countStudents(file) {
  const fileStream = fs.createReadStream(file);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  let headers = [];
  let headerProcessed = false;
  let studentCount = 0;
  let csStudentCount = 0;
  const csStudents = [];
  let sweStudentCount = 0;
  const sweStudents = [];

  rl.on('line', (line) => {
    if (!headerProcessed) {
      headers = line.split(',');
      headerProcessed = true;
    } else {
      const row = line.split(',');
      const rowObject = {};
      headers.forEach((header, index) => {
        rowObject[header.trim()] = row[index].trim();
      });
      studentCount += 1;
      if (rowObject.field === 'CS') {
        csStudentCount += 1;
        csStudents.push(rowObject.firstname);
      }
      if (rowObject.field === 'SWE') {
        sweStudentCount += 1;
        sweStudents.push(rowObject.firstname);
      }
    }
  });

  rl.on('close', () => {
    console.log(`Number of students: ${studentCount}`);
    console.log(`Number of students in CS: ${csStudentCount}. List: ${csStudents.join(', ')}`);
    console.log(`Number of students in SWE: ${sweStudentCount}. List: ${sweStudents.join(', ')}`);
  });

  rl.on('error', () => {
    throw new Error('Cannot load the database');
  });
}

module.exports = countStudents;
