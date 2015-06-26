from checkio_referee import RefereeCodeGolf
from checkio_referee import covercodes, representations, ENV_NAME


import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    DEFAULT_MAX_CODE_LENGTH = 250
    MAX_CODE_LENGHTS = {
        ENV_NAME.JS_NODE: 280
    }

    BASE_POINTS = 10
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.py_tuple_representation,
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_tuple,
    }
