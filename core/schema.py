from enum import Enum
from pydantic import BaseModel

class MetricType(str, Enum):
    BINARY = "binary"
    COUNT = "count"
    CONTINUOUS = "continuous"

class ExperimentRecord(BaseModel):
    user_id: str
    variant: str
    metric: float
    metric_type: MetricType
