const fs = require('fs');

function countStudents(file) {
  try {
    const data = fs.readFileSync(file, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const headers = lines[0].split(',');
    let studentCount = 0;
    let csStudentCount = 0;
    const csStudents = [];
    let sweStudentCount = 0;
    const sweStudents = [];

    for (let i = 1; i < lines.length; i += 1) {
      const row = lines[i].split(',');
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

    console.log(`Number of students: ${studentCount}`);
    console.log(`Number of students in CS: ${csStudentCount}. List: ${csStudents.join(', ')}`);
    console.log(`Number of students in SWE: ${sweStudentCount}. List: ${sweStudents.join(', ')}`);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
