import { createClient, print } from 'redis';

const client = createClient();
//If the client is ready log the ready message
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
// If an error occur log the error message
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (!err) {console.log(reply)}
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
