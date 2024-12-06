import { createQueue } from 'kue';

// function createJobData(phoneNumber, message) {
//   return {
//     phoneNumber,
//     message
//   }
// }
// create a queue using createQueue
const queue = createQueue();
const obj = {
  'phoneNumber': '07026705467',
  'message': 'Acct verified'
};
// Create a queue called push_notification_code to listen for jobs
const job = queue.create('push_notofication_code', obj).save(err => {
  if (!err) {console.log(`Notification job created: ${job.id}`)}
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.on('completed', () => {
  console.log('Notification job completed');
});
// create a new quese using kue
queue2 = createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
// using proces listen for new jobs on push_motification_code
queue2.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
