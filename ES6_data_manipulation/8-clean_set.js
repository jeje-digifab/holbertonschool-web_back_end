export default function cleanSet(set, startString) {
  const resultArray = [];
  for (const value of set) {
    if (startString && value.startsWith(startString)) {
      resultArray.push(value.slice(startString.length));
    }
  }
  return resultArray.join('-');
}
