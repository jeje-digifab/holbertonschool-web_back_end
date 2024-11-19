export default function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((student) => student.location === city);

  const updatedStudents = filteredStudents.map((student) => {
    const newGrade = newGrades.find((grade) => grade.studentId === student.id);

    let finalGrade;
    if (newGrade) {
      finalGrade = newGrade.grade;
    } else {
      finalGrade = 'N/A';
    }

    const updatedStudent = {
      ...student,
      grade: finalGrade,
    };

    return updatedStudent;
  });

  return updatedStudents;
}
