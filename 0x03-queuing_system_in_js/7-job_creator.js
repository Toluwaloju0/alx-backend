import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

queue = createQueue();

for (const obj in jobs) {
  const job = queue.create('push_notofication_code_2', obj).save(err => {
    if (!err) {console.log(`Notification job created: ${job.id}`)}
  });
  // listen for job handlers
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  }).on('complete', (result) => {
    console.log(`Notification job ${job.id} completed`);
  }).on('progress', (progress, data) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
}

const blacklisted = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (phoneNumber in blacklisted) {done(new Error(`Phone number ${phoneNumber} is blacklisted`))}
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue2 = createQueue();

queue2.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phonenumber, message, job, done)
})