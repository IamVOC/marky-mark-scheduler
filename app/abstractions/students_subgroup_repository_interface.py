from abc import ABC, abstractmethod
from typing import List


class IStudentsSubgroupRepository(ABC):

    @abstractmethod
    def get_students_chatid_by_subgroup(self, subgroup_id: int) -> List[int]:
        pass
