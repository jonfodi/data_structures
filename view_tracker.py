from abc import ABC, abstractmethod


class ViewTracker(ABC):
    @abstractmethod
    def record(self, page_id: str, ts: int) -> None: ...

    @abstractmethod
    def count_in_window(self, page_id: str, now: int) -> int: ...

    @abstractmethod
    def top_k(self, k: int, now: int) -> list[tuple[int, str]]: ...

    @abstractmethod
    def total_in_window(self, now: int) -> int: ...

    @abstractmethod
    def total_views_of_page(self, page_id) -> int: ...

    @abstractmethod
    def all_views(self) -> int: ...

    @abstractmethod
    def least_number_views(self, page_id) -> tuple: ...