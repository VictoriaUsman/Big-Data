csv_url = 'https://raw.githubusercontent.com/Azure/carprice/refs/heads/master/dataset/carprice.csv'
csv_path = 'car_data/carprice.csv'
duckdb_path = 'car_data/car_data.db'
import duckdb
import requests

def download_csv(csv_url: str, csv_path: str):
    response = requests.get(csv_url)
    response.raise_for_status()
    with open(csv_path, 'wb') as f:
        f.write(response.content)


import dagster as dg
import polars as pl

@dg.asset
def download_csv(context: dg.AssetExecutionContext):
    '''Download the csv file from the url'''
    context.log.info(f"Downloading csv file from")
    df = pl.read_csv(csv_url)
    df = df.with_columns([
        pl.col('normalized-losses').cast(pl.Float64, strict=False),
        pl.col('price').cast(pl.Float64, strict=False),
       
    ])
    df.write_csv(csv_path)

@dg.asset(deps=[download_csv])
def average_price(context: dg.AssetExecutionContext):
    """Calculate the average price of cars per make and store in DuckDB"""

    df = pl.read_csv(csv_path)
    df = df.drop_nulls(["price"])

    avg_df = (
        df.group_by("make")
          .agg(pl.col("price").mean().alias("average_price"))
    )

    average_data = [
        (row["make"], row["average_price"])
        for row in avg_df.to_dicts()
    ]

    with duckdb.connect(duckdb_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS average_price (
                make TEXT,
                average_price DOUBLE
            )
        """)
        conn.executemany(
            "INSERT INTO average_price VALUES (?, ?)",
            average_data
        )

        context.log.info(f"Inserted {len(average_data)} rows into DuckDB")

        conn.close()
