from __future__ import annotations

from django.conf import settings


def payments(request):
    return {"show_pricing": settings.USE_PAYMENTS}
