#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polisingos.settings.developmentmac")
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'polisingos.settings.production':
        sys.path.append('/usr/lib/pymodules/python2.7/flup')
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
