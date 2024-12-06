import createPushNotificationsJobs from '8-jobs';
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();

describe('Checking the queue and redis', () => {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit()
  });

  it('Checks the data inside the queue', () => {
    const jobs = [
      {
        phoneNumber: '07026706467',
        message: 'Tolu\'s number' 
      },
      {
        phoneNumber: '08071158452',
        message: 'Tolu\'s number Glo' 
      }
    ]
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
