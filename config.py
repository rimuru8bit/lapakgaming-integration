"""Configuration for Lapakgaming integration."""

from __future__ import annotations

import os

LAPAK_ENV = os.environ.get("LAPAK_ENV", "dev")  # dev|prod
LAPAK_SECRET_KEY = os.environ.get("LAPAK_SECRET_KEY", "")
LAPAK_BASE_URL_DEV = os.environ.get("LAPAK_BASE_URL_DEV", "https://dev.lapakgaming.com")
LAPAK_BASE_URL_PROD = os.environ.get("LAPAK_BASE_URL_PROD", "https://www.lapakgaming.com")
LAPAK_TIMEOUT_SECONDS = int(os.environ.get("LAPAK_TIMEOUT_SECONDS", "20"))
LAPAK_MAX_RETRIES = int(os.environ.get("LAPAK_MAX_RETRIES", "2"))

# Endpoint paths (adjust if provider path differs)
LAPAK_PATH_GET_CATEGORIES = os.environ.get("LAPAK_PATH_GET_CATEGORIES", "/api/reseller/categories")
LAPAK_PATH_GET_PRODUCTS = os.environ.get("LAPAK_PATH_GET_PRODUCTS", "/api/reseller/products")
LAPAK_PATH_GET_ALL_PRODUCTS = os.environ.get("LAPAK_PATH_GET_ALL_PRODUCTS", "/api/reseller/products/all")
