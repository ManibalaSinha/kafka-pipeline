from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class JobEvent:
    job_id: str
    user_id: str
    event_type: str   # created, updated, deleted
    status: str       # queued, running, completed, failed
    payload: dict
    timestamp: datetime

    @staticmethod
    def from_dict(data: dict) -> "JobEvent":
        return JobEvent(
            job_id=data["job_id"],
            user_id=data["user_id"],
            event_type=data["event_type"],
            status=data.get("status", "queued"),
            payload=data.get("payload", {}),
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )