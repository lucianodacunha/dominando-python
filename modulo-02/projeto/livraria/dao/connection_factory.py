import psycopg2
import os
from dotenv import load_dotenv


class ConnectionFactory:
    @staticmethod
    def get_connection():
        try:
            conn = psycopg2.connect(
                host = os.getenv('PGHOST'),
                dbname = os.getenv('PGDATABASE'),
                user = os.getenv('PGUSER'),
                password = os.getenv('PGPASSWORD'),
                sslmode = 'require'
            )
            return conn
        except Exception as e:
            print(f"Erro ao criar a conexão: {e}")
