import dagster as dg
from car_data.jobs import car_price_job  # ✅ correct absolute import

# Schedule runs every minute
car_price_schedule = dg.ScheduleDefinition(
    job=car_price_job,
    cron_schedule="* * * * *",  # 5 fields = every minute
)
