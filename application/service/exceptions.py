class BaseServiceError(Exception):
    pass


class UserNotFound(BaseServiceError):
    pass


class WrongPassword(BaseServiceError):
    pass


class WrongToken(BaseServiceError):
    pass
