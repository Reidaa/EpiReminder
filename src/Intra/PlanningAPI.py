from typing import List, Tuple

import requests

from API import API


class Activity:
    __json: dict

    def __init__(self, raw: dict = None):
        if raw is None:
            return
        if raw == "error":
            raise Exception()
        self.__json = raw

    @property
    def title(self) -> str:
        return self.raw["acti_title"]

    @property
    def raw(self) -> dict:
        return self.__json

    @property
    def start(self) -> Tuple[str, str]:
        thing = self.raw["start"]
        return thing.split()[0], thing.split()[1]

    @property
    def end(self) -> Tuple[str, str]:
        thing = self.raw["start"]
        return thing.split()[0], thing.split()[1]

    def is_registered(self) -> bool:
        thing = self.raw["event_registered"]
        return thing == "registered" or thing == "absent" or thing == "present"

    def is_present(self) -> bool:
        thing = self.raw["event_registered"]
        return True if thing == "present" else False

    def is_absent(self) -> bool:
        thing = self.raw["event_registered"]
        return thing == "absent"

    @property
    def what(self) -> str:
        return self.title

    @property
    def when(self) -> str:
        start = self.raw["start"].split()
        end = self.raw["end"].split()
        return "{start} - {end}".format(start=start[1][0:5], end=end[1][0:5])

    @property
    def where(self) -> str:
        return self.raw["room"]["code"].split('/')[-1]

    @property
    def codeinstance(self) -> str:
        return self.raw["codeinstance"]


class PlanningAPI(API):
    def __init__(self, username: str, token: str):
        API.__init__(self, username, token)
        self._url = "/planning/load?format=json&start={start}&end={end}"

    def get_raw_planning(self, start: str, end: str) -> requests.Response:
        return self._get(self._url.format(start=start, end=end))

    def get_planning(self, start=None, end=None) -> List[Activity]:
        activities: List[Activity] = []
        if start is None or end is None:
            pass
        else:
            response = self.get_raw_planning(start, end)
            for i, val in enumerate(response.json()):
                activities.append(Activity(val))
        return activities


if __name__ == "__main__":
    with open("../../log.txt") as file:
        lines = file.readlines()
    intra = PlanningAPI(lines[0], lines[1])
    intra.get_autolog_token()
    thing = intra.get_planning(start="2019-05-27", end="2019-05-29")
    print(thing[0].start, thing[0].title)
