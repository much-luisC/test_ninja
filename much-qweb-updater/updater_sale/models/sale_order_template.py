# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    report_header_text = fields.Html(string=_("Description before Table"))
    order_title = fields.Char(string=_("Title of the order"))
