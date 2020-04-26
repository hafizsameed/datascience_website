from __future__ import absolute_import
import time
import json
import logging
from dango_project.celery import app
from .models import Submission
from channels import Channel

log = logging.getLogger(__name__)

@app.task
def task1(sub_id, reply_channel):
    # time sleep represent some long running process
    time.sleep(3)
    print('hello world')
    # Change task status to completed
    # job = Job.objects.get(pk=job_id)
    # log.debug("Running job_name=%s", job.name)

    # job.status = "completed"
    # job.save()

    # Send status update back to browser client
    # if reply_channel is not None:
    #     Channel(reply_channel).send({
    #         "text": json.dumps ({
    #             "action": "completed",
    #             "job_id": job.id,
    #             "job_name": job.name,
    #             "job_status": job.status,
    #         })
    #     })

@app.task
def hello_world():
    time.sleep(3)
    print('hello world')