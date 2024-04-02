import strawberry
from strawberry.types import Info
from strawberry_django_jwt.decorators import login_required

from base.graphql.inputs import PaginationInput
from base.graphql.utils import get_paginator
from slots.graphql.types import PaginatedReservedSlotType
from slots.models import ReservedSlot


@strawberry.type
class ReservedSlotQuery:
    @strawberry.field(description="Returns a list of your reserved slots.")
    @login_required
    def my_reserved_slots(
        self, info: Info, pagination: PaginationInput | None = None
    ) -> PaginatedReservedSlotType:
        if pagination is None:
            pagination = {}
        user = info.context.request.user
        query = ReservedSlot.objects.filter(resource__user=user).order_by("-created")

        return get_paginator(
            query,
            pagination.page_size,
            pagination.page,
            PaginatedReservedSlotType,
        )
