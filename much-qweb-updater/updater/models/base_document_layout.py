from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ExtendedBaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    street = fields.Char(related="company_id.street", readonly=True)
    street2 = fields.Char(related="company_id.street2", readonly=True)
    zip = fields.Char(related="company_id.zip", readonly=True)
    city = fields.Char(related="company_id.city", readonly=True)
    company_registry = fields.Char(related="company_id.company_registry", readonly=True)
    managing_partner = fields.Char(related="company_id.managing_partner", readonly=True)

    header_address_position = fields.Selection(
        related="company_id.header_address_position", readonly=False, store=True
    )
    much_layout_style = fields.Selection(
        related="company_id.much_layout_style", readonly=False, store=True
    )
    much_tmpl = fields.Boolean(default=False, compute="_compute_much_template")
    logo_position = fields.Selection(
        related="company_id.logo_position", readonly=False, store=True
    )
    logo_width_unit = fields.Selection(
        related="company_id.logo_width_unit", readonly=False, store=True
    )
    logo_height_unit = fields.Selection(
        related="company_id.logo_height_unit", readonly=False, store=True
    )
    logo_width = fields.Integer(
        related="company_id.logo_width", readonly=False, store=True
    )
    logo_height = fields.Integer(
        related="company_id.logo_height", readonly=False, store=True
    )
    no_of_bank_accounts = fields.Selection(
        related="company_id.no_of_bank_accounts", readonly=False, store=True
    )

    @api.onchange("report_layout_id")
    def _compute_much_template(self):
        for wizard in self:
            wizard.much_tmpl = False
            if wizard.report_layout_id.name == "DIN 5008 – much. dynamic":
                wizard.much_tmpl = True

    def document_layout_save(self):
        """
        Raise warning if 'DIN 5008 – much. dynamic' is selected and
        'Much A4 for DIN5008' paper format is not selected.
        """
        if (
            self.paperformat_id != self.env.ref("updater.paperformat_much_din5008")
            and self.report_layout_id.name == "DIN 5008 – much. dynamic"
        ):
            raise UserError(
                _(
                    "'DIN 5008 – much. dynamic' layout works best with "
                    "'Much A4 for DIN5008' paper format."
                )
            )
        return super(ExtendedBaseDocumentLayout, self).document_layout_save()
