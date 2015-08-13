# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "$+qu#b5=3uwhkdf%ap&+-o2@jjs4=59#gjcpve%+#b^y89h-l7"
NEVERCACHE_KEY = "lin4vdpq-5vo%icy-c)0-+_s70d6jlbxje1p%)px(d@su(m!zq"

#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "karnblogdb",
        # Not used with sqlite3.
        "USER": "karn",
        # Not used with sqlite3.
        "PASSWORD": "karn",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}


###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }

