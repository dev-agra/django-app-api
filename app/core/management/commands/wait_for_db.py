"""
Django cmd to wait for db to be avlb
"""
import time
# psycopg2 operational error
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    # DJnago cmd to wait for db

    def handle(self, *arg, **options):
        """Entry point for cmd"""

        # Log mesg to screen
        self.stdout.write('Waiting for database....')
        # flag assume db is not up
        db_up = False
        while db_up is False:
            try:
                # if db is not ready exception block is run
                self.check(databases=['default'])
                # if no exception then db_up is True
                db_up = True
            except (Psycopg2Error, OperationalError):
                # If any error db is not available
                self.stdout.write('Database unavailable, waiting')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available'))
