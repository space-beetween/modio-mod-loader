from typing import Optional, Union
from pathlib import Path

import yaml


class Config:
    modio_api_key: str
    mod_directory_path: Path

    def __init__(
        self,
        modio_api_key: str,
        mod_directory_path: Optional[Union[str, Path]] = "mods"
    ) -> None:
        if isinstance(mod_directory_path, str):
            mod_directory_path = Path(mod_directory_path)

        kwargs = locals().copy()
        kwargs.pop('self')
        self.__dict__.update(kwargs)

    @classmethod
    def from_path(cls, path: Path):
        data = yaml.load(path.read_text("utf-8"), yaml.FullLoader)

        return cls(**data)


config = Config.from_path(Path("config.yml"))
