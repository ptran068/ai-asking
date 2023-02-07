from core.settings import env

# REPLICATION_DB_ALIAS = "replication"
# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
        "OPTIONS": {"charset": "utf8mb4", "init_command": "SET NAMES 'utf8mb4'"},
    },
    # REPLICATION_DB_ALIAS: {
    #     "ENGINE": "aicore.db_backend.mysql",
    #     "NAME": env("REPLICA_DB_NAME", default=env("DB_NAME")),
    #     "USER": env("REPLICA_DB_USER", default=env("DB_USER")),
    #     "PASSWORD": env("REPLICA_DB_PASS", default=env("DB_PASS")),
    #     "HOST": env("REPLICA_DB_HOST", default=env("DB_HOST")),
    #     "PORT": env("REPLICA_DB_PORT", default=env("DB_PORT")),
    #     "OPTIONS": {"charset": "utf8mb4", "init_command": "SET NAMES 'utf8mb4'"},
    # },
}


# DATABASE_ROUTERS = ["core.db_router.ReplicationRouter"]
# REPLICATED_DB_SLAVES = [REPLICATION_DB_ALIAS]
# REPLICATED_DB_DOWNTIME_CHECK_INTERVAL = 60
# REPLICATED_READ_ONLY_TRIES = 1
# REPLICATED_READ_ONLY_DOWNTIME = 20
# REPLICATED_CHECK_STATE_ON_WRITE = False
