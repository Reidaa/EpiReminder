import requests


class API:
    def __init__(self, username: str, autolog_token: str):
        self.base_url = "https://intra.epitech.eu/"
        self.username = username
        self.autolog_token = autolog_token

    def _get(self, request_url: str):
        if self.autolog_token is None:
            return None
        return requests.get(self.base_url + self.autolog_token + request_url)

    def check_log(self):
        is_token_valid: bool = self.check_token()
        is_username_valid: bool = self.check_username()
        return True if (is_token_valid is True and is_username_valid) is True else False

    def check_token(self) -> bool:
        return self.get_autolog_token().status_code == 200

    def check_username(self) -> bool:
        return self.get_student().status_code == 200

    def get_autolog_token(self):
        return self._get("/admin/autolog?format=json")

    def get_notification_coming(self):
        return self._get("/user/notification/coming?format=json")

    def get_notification_message(self):
        return self._get("/user/notification/message?format=json")

    def get_notification_alert(self):
        return self._get("/user/notification/alert?format=json")

    def get_notification_missed(self):
        return self._get("/user/notification/missed?format=json")

    def get_student(self):
        return self._get("/user/{username}?format=json".format(username=self.username))

    def get_student_notes(self):
        return self._get("/user/{username}/notes?format=json".format(username=self.username))

    def get_student_netsoul(self):
        return self._get("/user/{username}/netsoul?format=json".format(username=self.username))

    def get_student_binome(self):
        return self._get("/user/{username}/binome?format=json".format(username=self.username))


if __name__ == "__main__":
    with open("../../log.txt") as file:
        lines = file.readlines()
    intra = API(lines[0], lines[1])
    print(intra.check_log())
