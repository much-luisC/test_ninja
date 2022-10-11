# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Accounting",
    "summary": """
        Automatically update and set QWeb reports (Accounting)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    "category": "Technical",
    "version": "15.0.1.0.0",
    "license": "Other proprietary",
    # any module necessary for this one to work correctly
    "depends": ["base", "account", "updater"],
    "data": [
        "data/account/report_invoice_din5008.xml",
        "data/account/report_invoice_document_din5008_much.xml",
        "data/account/report_invoice_document_with_payments_din5008_much.xml",
        "data/account/report_invoice_with_payments_din5008.xml",
        "views/account_move.xml",
    ],
    "demo": [],
    "auto_install": True,
    "active": True,
}
