from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Repository:
    url: str
    endpoint: str
    secret: Optional[str] = None
    status_path: Optional[str] = None

@dataclass
class Configuration:
    host: str
    port: int
    repositories: List[Repository]
