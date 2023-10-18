from pymongo import MongoClient


class SaveReposts:
    def __init__(self):
        self.cliente = MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente["radar-pt"]
        self.collection = self.db.reports

    def saveReport(slaf, report):
        try:
            reports = self.db.reports
            reports.insert_one(report).inserted_id
        except Exception as error:
            print(error)
