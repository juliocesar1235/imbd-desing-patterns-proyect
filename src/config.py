import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    port = 5638
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "app")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"
