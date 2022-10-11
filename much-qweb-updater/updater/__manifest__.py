# -*- coding: utf-8 -*-
{
    "name": "much. QWeb Updater",
    "summary": """Automatically update and set QWeb templates""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de/",
    "category": "Technical Settings",
    "version": "15.0.1.0.0",
    "license": "Other proprietary",
    # any module necessary for this one to work correctly
    "depends": ["base", "web"],
    # external python (pip) dependencies
    # TODO: Add external dependencies when possible to
    # dynamically generate the ci/design of Odoo
    # "external_dependencies": {"python": ["libsass", "chevron"]},
    "data": [
        # TODO: related to dynamic ci/design of Odoo
        # "views/ir_settings.xml",
        "data/paper_format/much_paper_format_din5008.xml",
        "data/web/external_layout_din5008_much.xml",
        "data/report_layout/report_layout_custom.xml",
        "views/base_document_layout_views.xml",
        "views/res_company.xml",
    ],
    "demo": [],
    "application": True,
}
