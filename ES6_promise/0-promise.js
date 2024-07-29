function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true;
      if (success) {
        resolve('Success');
      } else {
        reject(new Error('Failure'));
      }
    }, 1000);
  });
}

export default getResponseFromAPI;
