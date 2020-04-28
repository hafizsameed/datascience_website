# from __future__ import absolute_import,unicode_literals
from celery import shared_task
from .models import Submission
from dango_project.celery import app
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync
# log = logging.getLogger(__name__)

# @shared_task
# def task1(sub_id, reply_channel):
    # time sleep represent some long running process
    # time.sleep(3)
    # print('hello world')
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

@shared_task
def hello_world():
    print('hello world')

# @app.task
# def hello_world():
#     # asyncio.sleep(3)
#     print('hello world')
#     return 1

@app.task
def check(chat_name,channel_name, sub):
    submission = Submission.objects.filter(id=sub).first()
    submission.verdict = 'accepted'
    submission.save()
    # sub.verdict = 'accepted'
    # sub.save()
    myResponse = {
        'id': sub,
        'verdict': 'accepted',
    }
    print('task is in progress')
    jsonform = json.dumps(myResponse)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'sameed_1',
        {
            'type': 'chat_message',
            'text': jsonform
        }
    )
