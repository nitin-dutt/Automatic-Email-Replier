import time
from app.scheduler import run_scheduler

if __name__ =="__main__":
    print("[Starting] Auto Email Replier...")
    while True:
        run_scheduler()
        time.sleep(300)
        
        