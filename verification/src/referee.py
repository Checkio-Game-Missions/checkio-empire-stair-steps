from checkio_referee import RefereeCodeGolf
from checkio_referee.covercode import py_tuple
from checkio_referee.representations import py_tuple_representation, base_representation

import settings
import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    DEFAULT_LENGTH = 250
    BASE_POINTS = 25
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "golf"
    CALLED_REPRESENTATIONS = {
        "python_3": py_tuple_representation,
        "javascript": base_representation
    }
    ENV_COVERCODE = {
        "python_2": py_tuple,
        "python_3": py_tuple,
        "javascript": None
    }
