from vkapi import config
from vkapi.session import Session

session = Session(config.VK_CONFIG["domain"], timeout=100)  # type: ignore