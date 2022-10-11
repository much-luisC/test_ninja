# -*- coding: utf-8 -*-
{
    "name": "much. | Updater CRM",
    "summary": """
        Enhancement for CRM with Updater DIN5008 Reports
    """,
    "description": """
        - Adds report_text field to CRM. Field will be printed on Sale/Invoice.
    """,
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    "category": "Technical",
    "version": "15.0.1.0.0",
    "license": "Other proprietary",
    # any module necessary for this one to work correctly
    "depends": ["base", "crm", "updater_account"],
    # always loaded
    "data": [
        "views/crm_team.xml",
        "data/account/report_invoice_document_din5008_much.xml",
    ],
    "demo": [],
    "auto_install": True,
    "active": True,
}
