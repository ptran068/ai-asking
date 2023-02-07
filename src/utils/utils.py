import random
import re
import string


class Utils:
    @staticmethod
    def id_generator(size=6, salt=""):
        prefix = ""
        if salt:
            import hashlib

            prefix = int(hashlib.sha1(salt.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        ran_str = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
        return f"{prefix}{ran_str}"