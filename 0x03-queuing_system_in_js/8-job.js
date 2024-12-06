export function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    for (const obj in jobs) {
      const job = queue.create('push_notification_code_3', obj).save(err => {
        if (!err) {console.log(`Notification job created: ${job.id}`)}
      });

      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      }).on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      }).on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`)
      })
    }
  } else {throw new Error('Jobs is not an array')}
}