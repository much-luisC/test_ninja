# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Sale",
    "summary": """
        Automatically update and set QWeb reports (Sales)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    "category": "Technical",
    "version": "15.0.1.0.0",
    "license": "Other proprietary",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "updater"],
    "data": [
        "data/sale/report_saleorder_din5008.xml",
        "data/sale/report_saleorder_document_din5008_much.xml",
        "views/sale_order.xml",
        "views/sale_order_template_views.xml",
    ],
    "demo": [],
    "auto_install": True,
    "active": True,
}
