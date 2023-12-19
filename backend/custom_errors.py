""" custom defined errors """


class DuplicateProductError(Exception):
    """ custom exception for duplicate product """
    def __init__(self, message="Duplicate product"):
        self.message = message
        super().__init__(self.message)

class DuplicateUserError(Exception):
    """ custom exception for duplicate user """
    def __init__(self, message="User exists"):
        self.message = message
        super().__init__(self.message)

class DuplicateVendorError(Exception):
    """ custom exception for duplicate user """
    def __init__(self, message="Vendor exists"):
        self.message = message
        super().__init__(self.message)

class UserNotFoundError(Exception):
    """ custom exception for user not found """
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)