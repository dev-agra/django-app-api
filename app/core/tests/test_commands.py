"""
Test custom management commands
"""
# for mocking
from unittest.mock import patch
# possiblities of error in database
from psycopg2 import OperationalError as Psycopg2Error
# call the command we testing
from django.core.management import call_command
# Exception
from django.db.utils import OperationalError
# Testing
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands"""
    def test_wait_for_db_ready(self, patched_check):
        """Test writing for db, if db ready"""
        # for this test return value true if ready
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting OperationalError"""
        # Raising some exception if delay
        """side effect allows us to pass obj
        independently to their type"""
        """first 2 times we call the mock method we
         raise Psycopg2Error and 3 times OperationalError"""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
