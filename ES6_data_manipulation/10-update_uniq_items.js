export default function updateUniqueItems(list) {
  list.forEach((value, key) => {
    if (value === 1) {
      list.set(key, 100);
    }
  });
}
