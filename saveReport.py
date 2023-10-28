from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class SaveReposts:
    def __init__(self):
        # mongodb+srv://lucasalmeida:lucasalmeida12@radar-pt.ial6lyr.mongodb.net/?retryWrites=true&w=majority
        # mongodb+srv://lucasalmeida:lucasalmeida12@radar-pt.3rljncc.mongodb.net/
        # self.cliente = MongoClient("mongodb://localhost:27017/radar-pt") # PARA RODAR NO LOCALHOST
        self.password = os.getenv("PASSWORD_DB")
        # SE FOR RODAR NO LOCAL COMENTAR A LINHA DE BAIXO
        self.cliente = MongoClient(f"mongodb+srv://lucasalmeida:{self.password}@radar-pt.3rljncc.mongodb.net/")
        self.db = self.cliente["radar-pt"]
        self.collection = self.db.reports

    def saveReport(self, report):
        try:
            reports = self.db.reports
            reports.insert_one(report).inserted_id
        except Exception as error:
            print("erro para inserir")
            print(error)
