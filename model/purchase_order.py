from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class purchase_order(models.Model):
    _inherit = 'purchase.order'
    _rec_name = "name"

    # partner_code = fields.Char()

    # @api.onchange('partner_id')
    # def get_partner(self):
    #     for rec in self:
    #         if rec.partner_id:
    #             partner = self.env['res.partner'].search(
    #                 [('id', '=', rec.partner_id.id)])
    #             if partner:
    #                 if len(partner) > 1:
    #                     rec.partner_code = False
    #                     # كود المورد مربوط بأكثر من مورد أو عميل يرجى المراجعة
    #                     raise ValidationError("The Vendor code is linked to more than one vendor , please review")

    #                 else:
    #                     rec.partner_code = partner.partner_code
    #             else:
    #                 rec.partner_code = False

    #         else:
    #             rec.partner_code = False
    #             rec.partner_id = False

    # @api.onchange('partner_code')
    # def get_partner_code(self):
    #     for rec in self:
    #         if rec.partner_code:
    #             partner = self.env['res.partner'].search(
    #                 [('partner_code', '=', rec.partner_code)])
    #             if partner:
    #                 if len(partner) > 1:
    #                     rec.partner_id = False
    #                     rec.partner_code = False

    #                     raise ValidationError("The Vendor code is linked to more than one vendor, please review")

    #                 else:
    #                     rec.write({'partner_id': partner.id})
