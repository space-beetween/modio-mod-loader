from typing import Optional, Tuple, Union, Any
import abc
import re


class AbstractScrapper(abc.ABC):
    pattern: re.Pattern

    @classmethod
    @abc.abstractmethod
    def scrap(cls, url: str) -> Optional[Tuple[Union[str, Any]]]:
        ...


class ModUrlScrapper(AbstractScrapper):
    pattern = re.compile(r'(?:https://)?mod.io/g/([^/]+)/m/([^/]+)')

    @classmethod
    def scrap(cls, url: str) -> Optional[Tuple[Union[str, Any]]]:
        """ Extracts the game id and mod id from the url """

        matches = cls.pattern.search(url)
        if matches is None:
            return None

        groups = matches.groups()
        if len(groups) != 2:
            return None

        return groups
