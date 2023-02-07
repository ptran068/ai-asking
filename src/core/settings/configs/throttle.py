from core.settings import env

AUTOMATION_COMPANY_IDS = env.json("AUTOMATION_COMPANY_IDS", default=[])
THROTTLE_WHITELIST_IPS = env.json("THROTTLE_WHITELIST_IPS", default=[])
