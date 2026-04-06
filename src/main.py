from extract import fetch_data
from transform import transform_data
from load import save_to_db

def run_pipeline():
    data = fetch_data()
    processed = transform_data(data)
    save_to_db(processed)

if __name__ == "__main__":
    run_pipeline()