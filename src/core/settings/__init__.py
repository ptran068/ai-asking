from os.path import exists
from os.path import dirname, join

# Use 12factor inspired environment variables or from a file
import environ

from django.db.models import ForeignKey
from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet

# NOTE: there are probably other items you'll need to monkey patch depending on
# your version.
for cls in [QuerySet, BaseManager, ForeignKey]:
    cls.__class_getitem__ = classmethod(lambda cls, *args, **kwargs: cls)  # type: ignore [attr-defined]

env = environ.Env()


# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(BASE_DIR), "config.env")
if not exists(env_file):
    env_file = "/etc/core/config.env"

if exists(env_file):
    environ.Env.read_env(str(env_file))

__version_info__ = {"major": 2, "minor": 1, "micro": 0, "releaselevel": "a", "serial": 0}


def get_version(short=False):
    vers = [
        "%(major)i.%(minor)i" % __version_info__,
    ]
    if __version_info__["micro"]:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__["releaselevel"] != "final" and not short:
        if __version_info__["serial"]:
            vers.append(".%i%s" % (__version_info__["serial"], __version_info__["releaselevel"][0]))
        else:
            vers.append("%s" % (__version_info__["releaselevel"][0]))
    return "".join(vers)


__version__ = get_version()
