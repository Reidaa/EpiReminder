from typing import List

import requests

from api import API


class Activity:
    __json: dict

    def __init__(self, raw: dict = None):
        if raw is None:
            return
        if raw == "error":
            raise Exception()
        self.__json = raw

    @property
    def raw(self) -> dict:
        return self.__json

    @property
    def title(self) -> str:
        return self.raw["title"]

    @property
    def events(self) -> list:
        return self.raw["events"]

    @property
    def type_title(self) -> str:
        return self.raw["type_title"]


class ModuleAPI(API):
    def __init__(self, username: str, token: str):
        API.__init__(self, username, token)
        self._url = "/module/{academicyear}/{codemodule}/{codeinstance}/?format=json"

    def get_raw_module(self, academicyear: str, codemodule: str, codeinstance: str) -> requests.Response:
        return self._get(self._url.format(academicyear=academicyear, codemodule=codemodule, codeinstance=codeinstance))

    def get_all_activities(self, academicyear: str, codemodule: str, codeinstance: str) -> List[Activity]:
        activities: List[Activity] = []
        response = self.get_raw_module(academicyear, codemodule, codeinstance)
        for i, val in enumerate(response.json()["activites"]):
            activities.append(Activity(val))
        return activities

    def get_user_activities(self, academicyear: str, codemodule: str, codeinstance: str):
        activities: List[Activity] = []
        response = self.get_raw_module(academicyear, codemodule, codeinstance)
        for i, val in enumerate(response.json()["activites"]):
            activities.append(Activity(val))
        activities = [i for i in activities if (len(i.events) != 0 and i.events[0]["user_status"] == "present")]
        return activities


if __name__ == "__main__":
    with open("../../log.txt") as file:
        lines = file.readlines()
    intra = ModuleAPI(lines[0], lines[1])
    thing = intra.get_raw_module("2018", "B-INN-000", "PAR-0-1").json()
    intra.get_user_activities("2018", "B-INN-001", "PAR-0-1")
    print()