from typing import Dict

DOMAIN = "sodexo"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:credit-card"
UNIT_OF_MEASUREMENT = "€"

ATTRIBUTION = "Data provided by https://www.sodexobeneficios.pt/"

LOGIN_URL = "https://login.sodexobeneficios.pt/login_processing.php"
MINHACONTA_URL = "https://minhaconta.sodexobeneficios.pt/"

LOGIN_URL_BR = "https://www.sodexobeneficios.com.br/sodexo-club/login/"

COUNTRY_PT = "Portugal"

CONF_COUNTRY = "country"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

CONF_COUNTRIES = [
    "Australia",
    "Belgium",
    "Brasil",
    "Canada",
    "Chile",
    "China",
    "Colombia",
    "Czech Republic",
    "Denmark",
    "Finland",
    "France",
    "India",
    "Indonesia",
    "Ireland",
    "Israel",
    "Italy",
    "Malaysia",
    "Mexico",
    "Middle East",
    "Netherlands",
    "Norway",
    "Peru",
    "Philippines",
    "Poland",
    COUNTRY_PT,
    "Qatar",
    "Romania",
    "Singapore",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Thailand",
    "Turkey",
    "United Arab Emirates",
    "United States",
    "United-Kingdom",
    "Vietnam"
]