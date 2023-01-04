from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import send_mail



def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(send_mail, 'interval', seconds=20)
	scheduler.start()