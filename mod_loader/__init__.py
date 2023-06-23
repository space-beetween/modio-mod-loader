import os

import modio

from .scrappers import ModUrlScrapper
from .downloaders import Downloader
from .config import config
from .exceptions import ModFileNotFound, WrongUrl


client = modio.Client(api_key=config.modio_api_key)


def download_mod(url: str) -> None:
    os.makedirs(config.mod_directory_path, exist_ok=True)

    mod_info = ModUrlScrapper.scrap(url)

    if mod_info is None:
        raise WrongUrl

    game_id, mod_id = mod_info

    game = client.get_game(f"@{game_id}")
    mod = game.get_mod(f"@{mod_id}")

    if mod.file is None:
        raise ModFileNotFound

    Downloader.download(
        mod.file.url,
        mod.file.filename,
        mod.file.size,
        config.mod_directory_path
    )
