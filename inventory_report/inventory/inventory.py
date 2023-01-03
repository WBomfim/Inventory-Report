from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        data = cls.__read_data(path)

        if type_report == "simples":
            return SimpleReport.generate(data)

        if type_report == "completo":
            return CompleteReport.generate(data)

    def __read_data(path):
        with open(path, "r") as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file))

            elif path.endswith(".json"):
                return json.load(file)

            elif path.endswith(".xml"):
                return xmltodict.parse(file.read())["dataset"]["record"]
