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
