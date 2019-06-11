import requests


class API:
    def __init__(self, username: str, token: str):
        self.base_url = "https://intra.epitech.eu/"
        self.username = username
        self.token = token
        if self.username is None or self.token is None:
            raise Exception("Wrong username and/or token")

    def _get(self, request_url: str) -> requests.Response:
        url = self.base_url + self.token + request_url
        response = requests.get(url)
        assert response.status_code == 200
        return response

    def get_current_academic_year(self) -> str:
        return self.get_student().json()["scolaryear"]

    def get_user_codeinstance(self) -> str:
        return "PAR-0-1"

    def check_log(self) -> bool:
        is_token_valid: bool = self.check_token()
        is_username_valid: bool = self.check_username()
        return True if (is_token_valid is True and is_username_valid) is True else False

    def check_token(self) -> bool:
        return self.get_autolog_token().status_code == 200

    def check_username(self) -> bool:
        return self.get_student().status_code == 200

    def get_autolog_token(self) -> requests.Response:
        return self._get("/admin/autolog?format=json")

    def get_notification_coming(self) -> requests.Response:
        return self._get("/user/notification/coming?format=json")

    def get_notification_message(self) -> requests.Response:
        return self._get("/user/notification/message?format=json")

    def get_notification_alert(self) -> requests.Response:
        return self._get("/user/notification/alert?format=json")

    def get_notification_missed(self) -> requests.Response:
        return self._get("/user/notification/missed?format=json")

    def get_student(self) -> requests.Response:
        return self._get("/user/{username}?format=json".format(username=self.username))

    def get_student_notes(self) -> requests.Response:
        return self._get("/user/{username}/notes?format=json".format(username=self.username))

    def get_student_netsoul(self) -> requests.Response:
        return self._get("/user/{username}/netsoul?format=json".format(username=self.username))

    def get_student_binome(self) -> requests.Response:
        return self._get("/user/{username}/binome?format=json".format(username=self.username))


if __name__ == "__main__":
    with open("../log.txt") as file:
        lines = file.readlines()
    intra = API(lines[0][:-1], lines[1][:-1]).get_student_notes().json()
    print(intra.check_log())
