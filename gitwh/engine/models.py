from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Repository:
    # Server URL
    url: str
    
    # this Server endpoint Path
    endpoint: str
    
    # Secret Key from Github Webhook setting
    secret: Optional[str] = None
    
    # Single file containing current progress, and progress info
    status_path: Optional[str] = None


@dataclass
class Configuration:
    host: str
    port: int
    repositories: List[Repository]
