import {
  uploadPhoto,
  createUser,
} from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((responses) => {
      const photoResponse = responses[0];
      const userResponse = responses[1];

      if (
        photoResponse
        && photoResponse.body
        && userResponse
        && userResponse.firstName
        && userResponse.lastName
      ) {
        console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
      } else {
        console.log('Signup system offline');
      }
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
