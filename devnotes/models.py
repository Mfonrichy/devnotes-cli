from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Note:
    text: str
    tags: list[str]
    created_at: str

    @staticmethod
    def create(text, tags):
        return Note(
            text=text,
            tags=tags,
            created_at=datetime.now().isoformat()
        )

    def to_dict(self):
        return asdict(self)