from typing import Optional, Union, Final
import abc
from pathlib import Path

import requests
from progress.bar import IncrementalBar


CHUNK_SIZE: Final[int] = 1024 * 5


class AbstractDownloader(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def download(
        self,
        url: str,
        filename: str,
        file_size: int,
        file_directory: Optional[Union[Path, str]] = Path()
    ) -> None:
        ...


class Downloader(AbstractDownloader):
    @classmethod
    def download(
        self,
        url: str,
        filename: str,
        file_size: int,
        file_directory: Optional[Union[Path, str]] = Path()
    ) -> None:
        file_path = Path(file_directory, filename)
        response = requests.get(url, stream=True)

        bar_max = file_size // CHUNK_SIZE + 1
        bar = IncrementalBar(
            filename,
            max=bar_max,
            suffix='%(percent).1f%% - %(elapsed)ds'
        )

        with file_path.open("wb") as file:
            for data in response.iter_content(CHUNK_SIZE):
                file.write(data)
                bar.next()
