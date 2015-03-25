from checkio_referee import RefereeCodeGolf
from checkio_referee import covercodes, representations

import settings
import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    DEFAULT_MAX_CODE_LENGTH = 250
    BASE_POINTS = 25
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    CALLED_REPRESENTATIONS = {
        "python_3": representations.py_tuple_representation,
        "python_2": representations.py_tuple_representation,
    }
    ENV_COVERCODE = {
        "python_2": covercodes.py_tuple,
        "python_3": covercodes.py_tuple,
        "javascript": None
    }
