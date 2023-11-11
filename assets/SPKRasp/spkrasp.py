import os
from pprint import pprint
from assets import Parser
from urllib import request
from pathlib import Path

dir_path = Path.cwd()
path_for_document = Path(dir_path, "assets", "info")


class SPKRasp:
    def __init__(self,  path=Path(path_for_document)):
        self.path = path
        self.filename = "current_rasp.xlsx"
        self.rasp = {} # Словарь с расписанием

        # Если документа с расписанием нет, тогда скачиваем
        if not Path(path_for_document, "current_rasp.xlsx").exists():
            self.download_rasp()

        self.start_parser()

    @staticmethod
    def download_rasp(filename: str = "current_rasp"):
        request.urlretrieve("http://spospk.ru/document/rasp/rasp.xlsx", f"assets/info/{filename}.xlsx")
        print("Расписание скачано.")

    def check_changes(self):
        SPKRasp.download_rasp("new_rasp")
        new_rasp = Path(path_for_document, "new_rasp.xlsx")
        is_changed = Parser(path=self.path, filename=self.filename).compare_rasp(new_rasp)
        if is_changed:
            os.remove(Path(path_for_document, "current_rasp.xlsx"))
            os.rename(new_rasp, Path(path_for_document, "current_rasp.xlsx"))
            print("Есть изменения.")
            self.start_parser()
        else:
            return "Изменений нет."

    def start_parser(self):
        self.rasp = Parser(path=self.path, filename=self.filename).start_parsing()

    def show_rasp(self, group: str = None, weektype: str = None, weekday: str = None):
        if group and not weektype and not weekday:
            pprint(self.rasp[group])
        elif group and weektype and not weekday:
            pprint(self.rasp[group][weektype])
        elif group and weektype and weekday:
            pprint(self.rasp[group][weektype][weekday])
        else:
            pprint(self.rasp)
