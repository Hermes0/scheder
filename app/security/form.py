from flask_security import LoginForm
from flask_security.confirmable import requires_confirmation
from flask_security.utils import _datastore, get_message, verify_and_update_password


class SchedLogin(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self):

        self.user = _datastore.get_user(self.email.data)

        if self.user is None:
            self.email.validate(self)
            self.email.errors.append("User or password invalid.")
            return False
        if not verify_and_update_password(self.password.data, self.user):
            self.password.errors.append(get_message('INVALID_PASSWORD')[0])
            return False
        if not self.user.password:
            self.password.errors.append(get_message('PASSWORD_NOT_SET')[0])
            return False
        if requires_confirmation(self.user):
            self.email.errors.append(get_message('CONFIRMATION_REQUIRED')[0])
            return False
        if not self.user.is_active:
            self.email.errors.append(get_message('DISABLED_ACCOUNT')[0])
            return False
        return True
