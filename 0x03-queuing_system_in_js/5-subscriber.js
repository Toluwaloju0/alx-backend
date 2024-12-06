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

// Suscribe to a channel called ALXchannel
client.subscribe('ALXchannel');
client.on('message', (channel, message) => {
  console.log(message)
  if (message === 'KILL_SERVER') {
    client.unsubscribe('ALXchannel');
    process.exit();
  }
});
