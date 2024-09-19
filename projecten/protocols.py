from dataclasses import dataclass

@dataclass
class Kandidaat():
    id: int
    naam: str
    stemmen: int