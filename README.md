![GitHub](https://img.shields.io/github/license/netsoft-ruidias/ha-custom-component-coverflex?style=for-the-badge)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/netsoft-ruidias/ha-custom-component-coverflex?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/netsoft-ruidias/ha-custom-component-coverflex?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/netsoft-ruidias/ha-custom-component-coverflex?style=for-the-badge)

# Coverflex Banefits Integration
Coverflex Benefits - Custom Component for Home Assistant

The data source for this integration is the [Coverflex Benefits](https://www.coverflex.com/).

The author of this project categorically rejects any and all responsibility for the card balance and other data that were presented by the integration.

# Installation
## HACS (Recommended)
This integration can be added to HACS as a custom (non-default) repository.

Assuming you have already installed and configured HACS, follow these steps:

1. Navigate to the HACS integrations page
2. Choose Integrations under HACS
3. Click the '+' button on the bottom of the page
4. Serch for "Coverflex", choose it, and click install in HACS
5. Ready! Now continue with the configuration.

## Configuration Through the interface
1. Navigate to `Settings > Devices & Services` and then click `Add Integration`
2. Search for `coverflex`
4. Enter your credentials
5. Repeat the procedure as many times as desired to include other cards you may have

# Presentation

To present your data (card balance) just use a any entity card

```yaml
type: entities
entities:
  - sensor.coverflex_card_firstName_lastName
```

## Transactions

While showing the card's balance on a card is commonplace (any entity card will do), displaying transactions can be more complicated to achieve.

We recommend using [custom:list-card](https://github.com/iantrich/list-card) which has the advantage of being able to indicate the number of rows to display:

```yaml
type: custom:list-card
entity: sensor.coverflex_card_firstName_lastName
feed_attribute: transactions
title: My Coverflex Transactions
row_limit: 10
columns:
  - title: Data
    field: date
  - title: Movimento
    field: description
  - title: Valor
    field: amount
    postfix: ' €'
    style:
      - text-align: right
      - white-space: nowrap
```

# Legal notice
This is a personal project and isn't in any way affiliated with, sponsored or endorsed by [Coverflex Benefits](https://www.coverflex.com/).

All product names, trademarks and registered trademarks in (the images in) this repository, are property of their respective owners. All images in this repository are used by the project for identification purposes only.

---
Please, support my other integrations: 
[Preços dos Combustivels](https://github.com/netsoft-ruidias/ha-custom-component-precoscombustiveis) | 
[MyEdenred](https://github.com/netsoft-ruidias/ha-custom-component-myedenred) |
[Sodexo](https://github.com/netsoft-ruidias/ha-custom-component-sodexo)
