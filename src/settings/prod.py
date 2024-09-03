from os import getenv
from pathlib import Path

ALLOWED_HOSTS = ["crimsonslate.com"]
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
INTERNAL_IPS = ["127.0.0.1"]
LANGUAGE_CODE = "en-us"
MEDIA_URL = "media/"
ROOT_URLCONF = "src.urls"
SECRET_KEY = getenv("CS_SECRET_KEY", "")
STATIC_URL = "static/"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "src.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("PSQL_NAME", "postgres"),
        "USER": getenv("PSQL_USER", "postgres"),
        "PASSWORD": getenv("PSQL_PASS", ""),
        "HOST": getenv("PSQL_HOST", "0.0.0.0"),
        "PORT": getenv("PSQL_PORT", "5432"),
    },
}

ECOM_USERDATA = {
    "NAME": "Crimson Slate",
    "ADDRESS": {
        "STREET": "123 Main St",
        "CITY": "Houston",
        "STATE": "TX",
        "ZIP": "77065",
    },
    "PHONE": {
        "MAIN": "+15555555555",
        "SUPPORT": "+15555555555",
        "SALES": "+15555555555",
    },
}

INSTALLED_APPS = [
    "ecom.apps.EcomConfig",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    "bucket": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "location": "media/",
            "access_key": getenv("AWS_ACCESS_KEY", ""),
            "secret_key": getenv("AWS_SECRET_KEY", ""),
            "bucket_name": getenv("AWS_BUCKET_NAME", ""),
            "verify": getenv("AWS_CERT_BUNDLE_PATH", False),
        },
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
