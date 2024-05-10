from typing import Any
from django.core.management.base import BaseCommand
from google_play_scraper import app


class Command(BaseCommand):

    help = "Create Apps in database"

    def handle(self, *args: Any, **options: Any) -> str | None:

        result = app(
            ""
        )
        return super().handle(*args, **options)