import abc
from typing import Any, Tuple


class ServiceBase(abc.ABC):
    def __init__(self) -> None:
        pass

    def perform(self) -> Tuple[bool, str, Any]:
        """Perform the service and return a tuple with the following values:
        - bool: True if the service was successful, False otherwise
        - str: A message describing the result of the service
        - Any: Any data that the service needs to return"""

        try:
            success, detail, data = self._perform()

            return success, detail, data
        except Exception as e:
            return False, str(e), None

    @abc.abstractmethod
    def _perform(self) -> Tuple[bool, str, Any]:
        pass
