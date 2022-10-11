# -*- coding: utf-8 -*-

from odoo import models, fields, _

LOGO_UNITS = [("px", "px"), ("in", "in"), ("%", "%")]


class Settings(models.Model):
    _inherit = "res.company"

    managing_partner = fields.Char(string="Managing Partner", default=False)

    header_address_position = fields.Selection(
        [("left", "Left"), ("center", "Center"), ("right", "Right")], default="left"
    )
    much_layout_style = fields.Selection(
        [("slick", "Slick"), ("colorful", "Colorful"), ("bw", "Black and White")],
        default="colorful",
    )
    logo_position = fields.Selection(
        [("left", "Left"), ("center", "Center"), ("right", "Right")], default="right"
    )
    logo_width_unit = fields.Selection(LOGO_UNITS, default="px")
    logo_width = fields.Integer(string=_("Width"))
    logo_height_unit = fields.Selection(LOGO_UNITS, default="px")
    logo_height = fields.Integer(string=_("Height"))
    no_of_bank_accounts = fields.Selection(
        [("1", "1"), ("2", "2")],
        default="1",
    )
