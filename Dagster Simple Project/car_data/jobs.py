import dagster as dg

# Define a job that includes all assets
car_price_job = dg.define_asset_job(
    name="car_price_job",
    selection=dg.AssetSelection.all()
)