import {
  uploadPhoto,
  createUser,
} from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      if (
        photoResponse && photoResponse.body
        && userResponse && userResponse.firstName
        && userResponse.lastName
      ) {
        console.log(
          `${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`,
        );
      } else {
        console.log('Signup system offline');
      }
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
