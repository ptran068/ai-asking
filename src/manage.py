#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # CHANGED manage.py will use development settings by
    # default. Change the DJANGO_SETTINGS_MODULE environment variable
    # for using the environment specific settings file.
    RUNNING_UNITTEST = "test" in sys.argv
    if RUNNING_UNITTEST:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.test")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
