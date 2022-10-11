# much. Qweb Updater Inventory DIN5008

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

- Added new template `report_delivery_much_custom_din5008` on **Stock** for 
  Delivery Slip Report

---

## Configuration

- User will need to configure the Document layout `external_layout_din5008_much` from **Settings**. 
- User will need to select the Paper Format `Much A4 for DIN5008 (paperformat_much_din5008)` from **Configure Document Layout**
- User will also need to select the `Header Address Position` and `Much Layout Style` from **Configure Document Layout**

---

## Usage

1. Print the Quotation/Order Report for Sales 

---

## Dependencies

### Odoo modules dependencies

| Module   | Why used?                         | Side effects 
|----------|-----------------------------------|--------------|
| Stock    | To print the delivery slip report |              |
| Updater  | To apply the report layout        |              |

### Python library dependencies

The module doesn't require any external Python library

---

## Limitations, Issues & Bugs

The module doesn't require any Limitations, Issues & Bugs

---

## Development

1. Added new report layout `report_delivery_document_din5008_much` for **Delivery Slip  
   Report**
2. Added new template view `report_deliveryslip_much_custom_din5008` on **Stock**

---

