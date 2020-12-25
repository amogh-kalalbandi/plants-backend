"""Auth Process functions."""

from apps.utils.common_utils import get_utc_time
from apps.utils.constants import ResponseConstants


class AuthProcessFunctions:
    """Auth Process function Class."""

    def logout_process_function(user):
        # Logout process."""
        resp_data = {}
        resp_data.update({
            ResponseConstants.ERROR_KEY.value: None,
            ResponseConstants.STATUS_KEY.value: ResponseConstants.STATUS_SUCCESS.value
        })
        # to invalidate the token on logout, as the token payload will have different login time
        user.last_login = get_utc_time()
        user.save()

        return resp_data
