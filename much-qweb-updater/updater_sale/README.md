# much. Qweb Updater Sale DIN5008

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

- Added new template `report_saleorder_much_custom_din5008` on **Sale** for 
  Quotation/Order Report

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

| Module          | Why used?                           | Side effects 
|-----------------|-------------------------------------|--------------|
| Sale            | To print the Quotation/Order report |              |
| Updater DIN5008 | To apply the report layout          |              |

### Python library dependencies

The module doesn't require any external Python library

---

## Limitations, Issues & Bugs

The module doesn't require any Limitations, Issues & Bugs

---

## Development

1. Added new report layout `report_saleorder_document_din5008_much` for **Quotation/Order Report**
2. Added new template view `report_saleorder_much_custom_din5008` on **Sale**
3. Added customer addresses in template based on the selection of the address as in original templates.
4. Added new fields `report_header_text and order_title` on **Sale Order**
5. Added new fields `report_header_text and order_title` on **Sale Quotation Template**
6. Overwrite `onchange_sale_order_template_id` method to add `Description before Table and Title of the order` from **Sale Quotation Template**.

---

