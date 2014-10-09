#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print(sys.path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
