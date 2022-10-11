# much. Qweb Updater DIN5008

**Table of Contents**

- Features & Limitations
- Configuration
- Usage
- Issues & Bugs
- Development
- Tests
- Dependencies

---

## Features

- Added a new Report Layout `external_layout_din5008_much`
- Added a new Paper Format `paperformat_much_din5008`
- Added new field `Header Address Position` on the **Company**
- Added new field `Much Layout Style` on the **Company** 
- Added new field `Header Address Position` on the **Base Document Layout**
- Added new field `Much Layout Style` on the **Base Document Layout**

---

## Configuration

User will need to configure the Document layout `external_layout_din5008_much` from 
**Settings**.
User will need to select the Paper Format `Much A4 for DIN5008 (paperformat_much_din5008)` from **Configure Document Layout**
User will also need to select the `Header Address Position` and `Much Layout Style` from **Configure Document Layout**

---

## Usage

1. User can print the report as per the Document layout selected `external_layout_din5008_much`

---

## Dependencies

### Odoo modules dependencies

| Module  | Why used?                           | Side effects 
|---------|-------------------------------------|--------------|
| Base    | Install the base modules            |              |
| Web     | To install web module to get fields |              |

### Python library dependencies

The module doesn't require any external Python library

---

## Limitations, Issues & Bugs

The module doesn't require any Limitations, Issues & Bugs

---

## Development

1. Added new fields `Header Address Position(header_address_position)`on the **Company**.
2. Added new fields `Much Layout Style(much_layout_style)`on the **Company**.
3. Added new fields `Header Address Position(header_address_position)`on the **Base Document Layout**.
4. Added new fields `Much Layout Style(much_layout_style)`on the **Base Document Layout**.
5. Added new fields `Logo Position(logo_position)`on the **Company**.
6. Added new fields `Logo Position(logo_position)`on the **Base Document Layout**.
7. Added new fields `logo_width, logo_width_unit, logo_height, logo_height_unit`on the **Company**.
8. Added new fields `logo_width, logo_width_unit, logo_height, logo_height_unit`on the **Base Document Layout**.
9. Added address header in `external_layout_din5008_much.xml` to be common for all.
10. Added tagline and logo position to be set based on the `Logo Position(logo_position)`
11. Added the layout background to the template as in the original templates `boxed, bold and striped`
12. Removed the dependencies of the updater module.
13. Added new field `Bank Accounts (no_of_bank_accounts)` on the **company** and 
    **Base Document Layout**
14. Added method to raise warning if `Much A4 for DIN5008` paper format is not selected on selection of `DIN 5008 – much. dynamic` layout.

---
