from astrapy import DataAPIClient

ASTRA_DB_TOKEN = "AstraCS:awecyutogdxJasErnuUxzwox:449fbd9abd77f015174ab632c421d1c81c10e44a7acf4837cf1e3ec327fb98af"
ASTRA_DB_ENDPOINT = "https://7dcac35d-65ec-44a9-8900-eb3c258cef30-us-east-2.apps.astra.datastax.com"
KEYSPACE = "keyspace1"

# Initialize the client
client = DataAPIClient(ASTRA_DB_TOKEN)
db = client.get_database_by_api_endpoint(
    ASTRA_DB_ENDPOINT,
    keyspace=KEYSPACE,
)

# Example: List collections in your keyspace
print(f"Connected to Astra DB: {db.list_collection_names()}")
