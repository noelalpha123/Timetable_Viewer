from supabase import Client, create_client

from config import Supabase_cred

url: str = Supabase_cred.url
key: str = Supabase_cred.key


supabase_client: Client = create_client(url, key)
