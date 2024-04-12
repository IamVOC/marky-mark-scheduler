from abc import ABC, abstractmethod
from typing import List


class IGroupRepository(ABC):

    @abstractmethod
    def get_all_groups(self) -> List[int]:
        pass
