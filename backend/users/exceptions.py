
class UsersAppError(Exception):
    pass


# ------
class InitiateRegistrationError(UsersAppError):
    pass


class InvalidRegistrationDataError(InitiateRegistrationError):
    pass

# ------
class CompleteRegistrationError(UsersAppError):
    pass


class LinkDoesNotExistError(CompleteRegistrationError):
    pass


class LinkIsExpiredError(CompleteRegistrationError):
    pass


class UserAlreadyExistsError(CompleteRegistrationError):
    pass

# ------
class ResendRegistrationEmailError(UsersAppError):
    pass


class EmailIsRequiredError(ResendRegistrationEmailError):
    pass


class UserIsAlreadyRegisteredError(ResendRegistrationEmailError):
    pass


class UserHasNoOldRegistrationLinksError(ResendRegistrationEmailError):
    pass
