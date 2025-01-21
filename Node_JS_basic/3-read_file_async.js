const fs = require('fs').promises;

function countStudents(file) {
  return fs.readFile(file, 'utf8')
    .then((data) => {
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
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
