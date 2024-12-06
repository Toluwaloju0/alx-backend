import { createClient, print } from 'redis';
import {promisify } from 'util';
import { createQueue } from 'kue';
import express from 'express';

const client = createClient();
//If the client is ready log the ready message
client.on('connect', () => {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function reserveSeat(number) {
  client.set('available_seats', number, print);
}

const get = promisify(client.get).bind(client);

async function getCurrentAvailableSeats() {
  return await get('available_seat');
}

reserveSeat(50);
let reservationEnabled = true;
// create a queue using kue
const queue = createQueue();
//create an app instance
const app = express();

app.get('/available_seats', (req, res) => {
  seats = getCurrentAvailableSeats();
  return res.json({'numberOfAvailableSeats': seats});
});
app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {return res.json({'status': 'Reservation are blocked'})}
  const job = queue.create('reserve_seat').save(err => {
    if (err) {return res.json({'status': 'Reservation failed'})}
    return res.json({'status': 'Reservation in process'})
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});
app.get('/process', (req, res) => {
  queue.process('reserve_seat', (job, done) => {
    // get the number of seats and decrease it
    const seat = getCurrentAvailableSeats() - 1;
    reserveSeat(seat);
    if (seat === 0) {
      reservationEnabled = false;
    }
    if (seat >= 0) {done()}
    else(done(new Error('Not enough seats available')))
  });
});
