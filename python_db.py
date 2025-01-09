from astrapy import DataAPIClient

ASTRA_DB_TOKEN = "AstraCS:awecyutogdxJasErnuUxzwox:449fbd9abd77f015174ab632c421d1c81c10e44a7acf4837cf1e3ec327fb98af"
ASTRA_DB_ENDPOINT = "https://7dcac35d-65ec-44a9-8900-eb3c258cef30-us-east-2.apps.astra.datastax.com"
KEYSPACE = "default_keyspace"

# Initialize the client
client = DataAPIClient(ASTRA_DB_TOKEN)
db = client.get_database_by_api_endpoint(
    ASTRA_DB_ENDPOINT,
    keyspace=KEYSPACE,
)
print(f"Connected to Astra DB: {db.list_collection_names()}")

collection_name="gravity_levelmind"

# collection = db.collection(collection_name)

social_media_data = [
    {"post_id": "1", "post_type": "carousel", "likes": 120, "comments": 30, "shares": 15, "date": "2025-01-01"},
    {"post_id": "2", "post_type": "reel", "likes": 200, "comments": 50, "shares": 40, "date": "2025-01-01"},
    {"post_id": "3", "post_type": "static_image", "likes": 90, "comments": 20, "shares": 10, "date": "2025-01-01"},
    {"post_id": "4", "post_type": "carousel", "likes": 150, "comments": 35, "shares": 20, "date": "2025-01-02"},
    {"post_id": "5", "post_type": "reel", "likes": 300, "comments": 70, "shares": 60, "date": "2025-01-02"},
    {"post_id": "6", "post_type": "static_image", "likes": 110, "comments": 25, "shares": 12, "date": "2025-01-02"},
    {"post_id": "7", "post_type": "carousel", "likes": 170, "comments": 40, "shares": 25, "date": "2025-01-03"},
    {"post_id": "8", "post_type": "reel", "likes": 250, "comments": 60, "shares": 50, "date": "2025-01-03"},
    {"post_id": "9", "post_type": "static_image", "likes": 80, "comments": 18, "shares": 8, "date": "2025-01-03"}
]


collection = db.get_collection(collection_name)  # The crucial change: call the collection
print(f"Collection '{collection_name}' accessed successfully!")
result=collection.insert_many(social_media_data)
print(f"Inserted documents: {result}")