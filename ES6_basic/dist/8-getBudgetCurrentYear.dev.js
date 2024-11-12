"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = getBudgetForCurrentYear;

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function getCurrentYear() {
  var date = new Date();
  return date.getFullYear();
}

function getBudgetForCurrentYear(income, gdp, capita) {
  var _budget;

  var budget = (_budget = {}, _defineProperty(_budget, "income-".concat(getCurrentYear()), income), _defineProperty(_budget, "gdp-".concat(getCurrentYear()), gdp), _defineProperty(_budget, "capita-".concat(getCurrentYear()), capita), _budget);
  return budget;
}