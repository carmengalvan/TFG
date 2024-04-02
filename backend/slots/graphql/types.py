from datetime import time

import strawberry

from base.graphql.types import PaginatedQueryType
from resources.graphql.types import ResourceType


@strawberry.type
class ReservedSlot:
    resource: ResourceType
    name: str
    description: str
    email: str
    start_time: time
    end_time: time


@strawberry.type
class PaginatedReservedSlotType(PaginatedQueryType):
    edges: list[ReservedSlot]
