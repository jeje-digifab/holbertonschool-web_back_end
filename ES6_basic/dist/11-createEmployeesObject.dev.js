"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = createEmployeesObject;

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function createEmployeesObject(departmentName, employees) {
  return _defineProperty({}, departmentName, employees);
}