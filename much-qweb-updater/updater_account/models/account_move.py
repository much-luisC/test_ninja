# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _


class AccountMove(models.Model):
    _inherit = "account.move"

    report_header_text = fields.Html(string=_("Description before Table"))
    order_title = fields.Char(string=_("Title of the order"))
