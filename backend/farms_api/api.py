import csv
import glob
from fastapi import FastAPI
from farms_api.datastore import InMemoryDataStore

storage = InMemoryDataStore()

app = FastAPI(
    title="Solita Dev Academy Farms API",
    description="Made by Anastasiia Erokhina"
)

@app.post("/init")
async def init_api():
    """
    Loads data from CSV files into datastore. Also adds some additional info about the farms.
    """
    print("initting")
    data_directory = "./csv_data"
    csv_files = glob.glob(f"{data_directory}/*.csv")
    print(csv_files)
    for file_path in csv_files:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                storage.add_stat_data(line)
    return {}

@app.get("/v1/farms")
async def get_all_farms():
    """
    Returns info about all farms.
    """
    return {}

@app.get("/v1/farms/{farm_id}")
async def get_farm_details():
    """
    Returns info about a specific farm.
    """
    return {}

@app.get("/v1/farms/{farm_id}/stats")
async def get_all_farm_stats():
    """
    Returns all stats for a farm.
    """
    return {}

@app.get("/v1/farms/{farm_id}/stats/{sensor_type}/monthly")
async def get_monthly_stats_by_farm_sensor():
    """
    Returns stats for a given sensor, for a given farm, aggregated monthly.
    """
    return {}
