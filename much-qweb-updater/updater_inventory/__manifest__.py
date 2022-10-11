# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Inventory",
    "summary": """
        Automatically update and set QWeb reports (Inventory)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    "category": "Technical",
    "version": "15.0.1.0.0",
    "license": "Other proprietary",
    # any module necessary for this one to work correctly
    "depends": ["base", "stock", "updater"],
    "data": [
        "data/inventory/report_deliveryslip_din5008.xml",
        "data/inventory/report_delivery_document_din5008_much.xml",
    ],
    "demo": [],
    "auto_install": True,
    "active": True,
}
