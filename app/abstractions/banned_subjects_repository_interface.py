from abc import ABC, abstractmethod
from typing import List


class IBannedSubjectsRepository(ABC):

    @abstractmethod
    def get_all_subjects(self) -> List[int]:
        pass
