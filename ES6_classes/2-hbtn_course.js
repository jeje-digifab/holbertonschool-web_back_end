export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = String;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = Number;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this._students = Array;
  }
}
