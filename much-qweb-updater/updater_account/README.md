# much. Qweb Updater Account DIN5008

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

- Added new template `report_purchaseorder_much_custom_din5008` on **Account** for Invoices without Payment Report
- Added new template `report_invoice_with_payments_much_custom_din5008` on **Account** for Invoice Report

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

| Module          | Why used?                                             | Side effects 
|-----------------|-------------------------------------------------------|--------------|
| Account         | To print the Invoices/Invoices without Payment report |              |
| Updater DIN5008 | To apply the report layout                            |              |

### Python library dependencies

The module doesn't require any external Python library

---

## Limitations, Issues & Bugs

The module doesn't require any Limitations, Issues & Bugs

---

## Development

1. Added new report layout `report_invoice_document_din5008_much` for **Invoice without Payment**
2. Added new report layout `report_invoice_document_with_payments_din5008_much` for **Invoice**
3. Added new template view `report_invoice_much_custom_din5008` on **Account**
4. Added new template view `report_invoice_with_payments_much_custom_din5008` on **Account**
5. Added new fields `report_header_text and order_title` on **Account**

---

