from odoo import models, fields

class Products(models.Model):
    _name = 'umkm.products'
    _description = 'UMKM Products'
    _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]

    profile_id = fields.Many2one('umkm.profile', string='UMKM Profile')
    name = fields.Char(string='Nama Produk', required=True)
    _type = fields.Selection([
            ('makanan_kemasan', 'Makanan Kemasan'),
            ('minuman_kemasan', 'Minuman Kemasan'),
            ('makanan_cepatsaji', 'Makanan Cepat Saji'),
            ('makanan_frozen', 'Makanan Frozen'),
            ('kerajinan_tangan', 'Kerajinan Tangan'),
            ('produk_lainnya', 'Produk Lainnya')
        ], string='Tipe', required=True)
    description = fields.Text(string='Deskripsi')
    komposisi = fields.Text(string='Komposisi')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    price = fields.Monetary(string='Harga', currency_field='currency_id')
    netto = fields.Integer(string='Netto (gram/ml)')
    pirt_no = fields.Char(string='No. PIRT')
    pirt_file = fields.Binary(string='File PIRT', attachment=True)
    halal_no = fields.Char(string='No. Halal')
    halal_file = fields.Binary(string='File Halal', attachment=True)
    bpom_no = fields.Char(string='No. BPOM')
    bpom_file = fields.Binary(string='File BPOM', attachment=True)
    kemasan_type = fields.Selection([
            ('plastik', 'Plastik'),
            ('kardus', 'Kardus'),
            ('kaleng', 'Kaleng'),
            ('botol', 'Botol'),
            ('lainnya', 'Lainnya')
        ], string='Tipe Kemasan', required=True)
    kemasan_file = fields.Binary(string='File Kemasan', attachment=True)
    