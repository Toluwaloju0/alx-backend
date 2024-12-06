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

// Get an object for to store in the client
const objects = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
};
// iterate through object and use hset to set the value of the field
for (const key in objects) {
  client.hset('ALX', key, objects[key], print);
}

client.hgetall('ALX', (err, reply) => {
  if (!err) {console.log(reply)}
});
