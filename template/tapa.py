from typing import Dict, Any, List

from tapas.params import Parameter
from tapas.tools.git import TAPAS_SYSTEM_INIT_GIT_PARAMETER
from tapas.tools.license import TAPAS_SYSTEM_LICENSE_PARAMETER


def get_params() -> List[Parameter]:
    """
    :return: List of parameter descriptions to prompt user
    """
    return [
        TAPAS_SYSTEM_LICENSE_PARAMETER,
        TAPAS_SYSTEM_INIT_GIT_PARAMETER,
    ]


def post_init(params: Dict[str, Any]) -> int:
    """
    :param params: dictionary of parameters entered by user
    :return: Error code. Will stop generation if not zero
    """
    return 0
