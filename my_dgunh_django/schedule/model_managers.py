from django.db import models
from collections.abc import MutableMapping
from typing import Any


class student_schedule_manager(models.Manager):

    def get_or_create(self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any) -> tuple[Any, bool]:
        return super().get_or_create(defaults, **kwargs)
