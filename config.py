import os

from dotenv import load_dotenv

load_dotenv()


class Supabase_cred:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")


class AppData:
    sec = os.environ.get()
