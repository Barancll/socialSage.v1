from apscheduler.schedulers.blocking import BlockingScheduler
import main

def start_scheduler():
    scheduler = BlockingScheduler()
    # Her Pazartesi 09:00'da run_pipeline fonksiyonunu çalıştırır.
    scheduler.add_job(main.run_pipeline, 'cron', day_of_week='mon', hour=9, minute=0)
    try:
        print("Zamanlayıcı başladı. Planlı görev bekleniyor...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Zamanlayıcı durdu.")

if __name__ == "__main__":
    start_scheduler()