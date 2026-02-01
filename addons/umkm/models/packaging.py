from odoo import models, fields

class Packaging(models.Model):
    _name = 'umkm.packaging'
    _description = 'UMKM Product Packaging'

    product_id = fields.Many2one('umkm.products', string='Product', required=True, ondelete='cascade')
    type = fields.Selection([
        ('plastik', 'Plastik'),
        ('kardus', 'Kardus'),
        ('kaleng', 'Kaleng'),
        ('botol', 'Botol'),
        ('lainnya', 'Lainnya')
    ], string='Packaging Type', required=True)
    netto = fields.Integer(string='Netto', required=True, default=100)
    netto_unit = fields.Selection([
        ('gram', 'Gram'),
        ('ml', 'ml'),
    ], string='Unit', required=True, default='gram')
    netto_display = fields.Char(string='Netto Display', compute='_compute_netto_display', store=False)
    packaging_file = fields.Binary(string='Packaging File', attachment=True)
    packaging_file_name = fields.Char(string='File Name')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    price = fields.Monetary(string='Price', currency_field='currency_id')
    price_display = fields.Char(string='Price Display', compute='_compute_price_display', store=False)

    def _compute_netto_display(self):
        for record in self:
            if record.netto:
                record.netto_display = f"{record.netto} {record.netto_unit}"
            else:
                record.netto_display = ''

    def _compute_price_display(self):
        for record in self:
            if record.price:
                # Format price with dot as thousand separator and no decimal places
                price_formatted = "{:,.0f}".format(record.price).replace(',', '.')
                record.price_display = f"Rp {price_formatted}"
            else:
                record.price_display = ''