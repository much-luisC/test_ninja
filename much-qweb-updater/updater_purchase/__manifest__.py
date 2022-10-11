# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Purchase",
    "summary": """
        Automatically update and set QWeb reports (Purchase)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    "category": "Technical",
    "version": "15.0.1.0.0",
    "license": "Other proprietary",
    # any module necessary for this one to work correctly
    "depends": ["base", "purchase", "updater"],
    "data": [
        "data/purchase/report_purchaseorder_din5008.xml",
        "data/purchase/report_purchaseorder_document_din5008_much.xml",
        "data/purchase/report_purchasequotation_din5008.xml",
        "data/purchase/report_purchasequotation_document_din5008_much.xml",
        "views/purchase_order_views.xml",
    ],
    "demo": [],
    "auto_install": True,
    "active": True,
}
