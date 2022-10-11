# -*- coding: utf-8 -*-
from odoo import fields, models, _, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    report_header_text = fields.Html(string=_("Description before Table"))
    order_title = fields.Char(string=_("Title of the order"))

    @api.onchange("sale_order_template_id")
    def onchange_sale_order_template_id(self):
        ret = super(SaleOrder, self).onchange_sale_order_template_id()
        if self.sale_order_template_id:
            template = self.sale_order_template_id.with_context(
                lang=self.partner_id.lang
            )
            self.report_header_text = template.report_header_text
            self.order_title = template.order_title
        return ret
