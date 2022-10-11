# much. Qweb Updater Purchase DIN5008

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

- Added new template `report_purchaseorder_much_custom_din5008` on **Purchase** for 
  Purchase Order Report
- Added new template `report_purchasequotation_much_custom_din5008` on **Purchase** for 
  Purchase Order Report

---

## Configuration

- User will need to configure the Document layout `external_layout_din5008_much` from **Settings**. 
- User will need to select the Paper Format `Much A4 for DIN5008 (paperformat_much_din5008)` from **Configure Document Layout**
- User will also need to select the `Header Address Position` and `Much Layout Style` from **Configure Document Layout**

---

## Usage

1. Print the Quotation/Order Report for Purchase 
2. Print the Request for Quotation Report for Purchase

---

## Dependencies

### Odoo modules dependencies

| Module          | Why used?                          | Side effects 
|-----------------|------------------------------------|--------------|
| Purchase        | To print the Purchase Order report |              |
| Updater DIN5008 | To apply the report layout         |              |

### Python library dependencies

The module doesn't require any external Python library

---

## Limitations, Issues & Bugs

The module doesn't require any Limitations, Issues & Bugs

---

## Development

1. Added new report layout `report_purchaseorder_document_din5008_much` for **Purchase Order Report**
2. Added new template view `report_purchaseorder_much_custom_din5008` on **Purchase**
3. Added new template view `report_purchasequotation_much_custom_din5008` on **Purchase**
4. Added new report layout `report_purchasequotation_document_din5008_much` for **Request for Quotation Report**
5. Added new fields `report_header_text and order_title` on **Purchase**

---

