from odoo import  models, fields, _
from odoo.exceptions import ValidationError

class res_partner(models.Model):
    _inherit = "res.partner"
  
    def write(self, vals):
        allow_change_accounts = self.user_has_groups("yousentech_accounting_partners.allow_change_partner_account_group" )
        purchase_order =[]
        sale_order =[]

        for rec in self:
            partner = self.env["res.partner"].search([("id", "=", rec.id)])
            partner_moves = self.env["account.move.line"].search([("partner_id", "=", rec.id)])
            if self.env["ir.module.module"].search(
            [("name", "=", "sale")]).state  =='installed':
                sale_order = self.env["sale.order"].search([("partner_id", "=", rec.id)])
            if self.env["ir.module.module"].search(
            [("name", "=", "purchase")]).state  =='installed':
                purchase_order = self.env["purchase.order"].search([("partner_id", "=", rec.id)])

            # partner_name = partner.name
            partner_account_receivable = partner.property_account_receivable_id.id
            partner_account_payable = partner.property_account_payable_id.id
            # check accounts changes
            if not allow_change_accounts:
                if vals.get("property_account_payable_id"):
                    if partner_account_payable != vals.get("property_account_payable_id"):
                        if partner_moves:
                            # لا يمكن تغيير حساب الموردين لوجود فواتير مسبقة له
                            raise ValidationError(_("Cannot change account payable for a partner with existing invoices" ))

                if vals.get("property_account_receivable_id"):
                    if partner_account_receivable != vals.get("property_account_receivable_id"):
                        if partner_moves:
                            # لا يمكن تغيير حساب العملاء لوجود فواتير مسبقة له
                            raise ValidationError(_ ("Cannot change account receivable for a partner with existing invoices"))
                            
        res = super(res_partner, self).write(vals)
        return res

  



 


