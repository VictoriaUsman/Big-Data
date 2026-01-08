from dagster import Definitions, load_assets_from_modules
from car_data import assets
from car_data.jobs import car_price_job
from car_data.schedule import car_price_schedule

all_assets = load_assets_from_modules([assets])
all_jobs = [car_price_job]
all_schedules = [car_price_schedule]

defs = Definitions(
    assets=all_assets,
    jobs=all_jobs,
    schedules=all_schedules
)
