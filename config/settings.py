import os
from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv
from import_export.formats.base_formats import CSV, XLSX

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.import_export",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "import_export",
    "apps.common",
    "apps.institutions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

IMPORT_FORMATS = [CSV, XLSX]

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

# Unfold
UNFOLD = {
    "SITE_TITLE": "VetMap Admin",
    "SITE_HEADER": "VetMap Admin",
    "SITE_URL": "/",
    "SITE_ICON": lambda request: static("images/icon.png"),
    "SITE_LOGO": lambda request: static("images/icon.png"),
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("images/middleware.svg"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": False,
    "ENVIRONMENT": "apps.common.views.environment_callback",
    "LOGIN": {
        "image": lambda request: static("images/login.jpg"),
        "redirect_after": lambda request: reverse_lazy("admin:index"),
    },
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "SIDEBAR": {
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Administrator"),
                "separator": True,
                "items": [
                    {
                        "title": _("Users & Groups"),
                        "icon": "people",
                        "permission": lambda request: request.user.is_superuser,
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
            {
                "title": _("Map"),
                "separator": True,
                "items": [
                    {
                        "title": _("Institutions"),
                        "icon": "school",
                        "link": reverse_lazy("admin:institutions_institution_changelist"),
                    },
                ],
            },
        ],
    },
    "TABS": [
        {
            "models": [
                "auth.user",
                "auth.group",
            ],
            "items": [
                {
                    "title": _("Users"),
                    "link": reverse_lazy("admin:auth_user_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Groups"),
                    "link": reverse_lazy("admin:auth_group_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                },
            ],
        }
    ],
}

REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%SZ",
    "PAGE_SIZE": 50,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Vet Map API",
    "DESCRIPTION": "Schema for API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
}

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "INFO")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s]- %(message)s"},
    },
    "handlers": {
        "console": {
            "level": LOGGING_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "info": {"handlers": ["console"], "level": LOGGING_LEVEL, "propagate": True},
        "django": {"handlers": ["console"], "level": LOGGING_LEVEL, "propagate": True},
    },
}
