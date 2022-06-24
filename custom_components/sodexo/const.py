from typing import Dict

DOMAIN = "sodexo"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:credit-card"
UNIT_OF_MEASUREMENT = "€"

LOGIN_URL = "https://login.sodexobeneficios.pt/login_processing.php"
MINHACONTA_URL = "https://minhaconta.sodexobeneficios.pt/"

COUNTRY_PT = "Portugal"
COUNTRY_BR = "Brasil"

COUNTRIES: Dict[str, str] = { 
    "pt": "Portugal", 
    "br": "Brasil" 
} 