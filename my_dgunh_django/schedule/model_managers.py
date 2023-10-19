from django.db import models
from collections.abc import MutableMapping
from typing import Any

from django.db.models.query import QuerySet


class student_schedule_manager(models.Manager):
    

    def get_or_create(self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any) -> tuple[Any, bool]:
        return super().get_or_create(defaults, **kwargs)


    def get_queryset(self) -> QuerySet:
        return super().get_queryset()
    

    def contains(self, obj: Any) -> bool:
        return super().contains(obj)

    
    def get_group_info(self):
        return 
    

class teacher_manager(models.Manager):
    

    def get_or_create(self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: Any) -> tuple[Any, bool]:
        return super().get_or_create(defaults, **kwargs)


    def get_queryset(self) -> QuerySet:
        return super().get_queryset()
    

    def contains(self, obj: Any) -> bool:
        return super().contains(obj)
    