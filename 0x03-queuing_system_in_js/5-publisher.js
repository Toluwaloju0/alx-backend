import { createClient } from 'redis';

const client = createClient();
//If the client is ready log the ready message
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
// If an error occur log the error message
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

async function publishMessage(message, time) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  console.log(`About to send ${message}`);
  client.publish('ALXchannel', message);
}

publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
