from abc import ABC, abstractmethod
from typing import List


class IStudentsGroupRepository(ABC):

    @abstractmethod
    def get_students_chatid_by_group(self, group_id: int) -> List[int]:
        pass
