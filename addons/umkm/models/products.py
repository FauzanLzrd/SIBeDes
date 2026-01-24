from odoo import models, fields, api

class Products(models.Model):
    _name = 'umkm.products'
    _description = 'UMKM Products'
    _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]

    profile_id = fields.Many2one('umkm.profile', string='Usaha')
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
    price_display = fields.Char(string='Harga Display', compute='_compute_price_display', store=False)
    netto = fields.Integer(string='Netto')
    netto_unit = fields.Selection([
            ('gram', 'Gram'),
            ('ml', 'ml'),
        ], string='Unit', default='gram')
    netto_display = fields.Char(string='Netto Display', compute='_compute_netto_display', store=False)
    pirt_status = fields.Selection([('not_needed', 'Tidak Memerlukan'),
            ('potential_not_have', 'Belum Memiliki'),
            ('potential_progress', 'Proses Pembuatan'),
            ('owned', 'Memiliki'),
            ('owned_created', 'Dibuat oleh Tim'),
        ], string='Status PIRT')
    pirt_no = fields.Char(string='No. PIRT')
    pirt_file = fields.Binary(string='File PIRT', attachment=True)
    halal_status = fields.Selection([('not_needed', 'Tidak Memerlukan'),
            ('potential_not_have', 'Belum Memiliki'),
            ('potential_progress', 'Proses Pembuatan'),
            ('owned', 'Memiliki'),
            ('owned_created', 'Dibuat oleh Tim'),
        ], string='Status Halal')
    halal_no = fields.Char(string='No. Halal')
    halal_file = fields.Binary(string='File Halal', attachment=True)
    bpom_status = fields.Selection([('not_needed', 'Tidak Memerlukan'),
            ('potential_not_have', 'Belum Memiliki'),
            ('potential_progress', 'Proses Pembuatan'),
            ('owned', 'Memiliki'),
            ('owned_created', 'Dibuat oleh Tim'),
        ], string='Status BPOM')
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
    image = fields.Binary(string='Foto', attachment=True, tracking=True)

    @api.depends('price')
    def _compute_price_display(self):
        for record in self:
            if record.price:
                # Format price with dot as thousand separator and no decimal places
                price_formatted = "{:,.0f}".format(record.price).replace(',', '.')
                record.price_display = f"Rp {price_formatted}"
            else:
                record.price_display = ''

    @api.depends('netto', 'netto_unit')
    def _compute_netto_display(self):
        for record in self:
            if record.netto:
                record.netto_display = f"{record.netto} {record.netto_unit}"
            else:
                record.netto_display = ''

    @api.model
    def create(self, vals):
        # Log to diagnose where products are being created from
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info("=== PRODUCT CRECTION DIAGNOSIS ===")
        _logger.info(f"Context keys: {self.env.context.keys()}")
        _logger.info(f"Context values: {dict(self.env.context)}")
        _logger.info(f"vals: {vals}")
        _logger.info(f"Has profile_id in vals: {'profile_id' in vals}")
        _logger.info(f"Has default_profile_id in context: {'default_profile_id' in self.env.context}")
        _logger.info("=====================================")
        
        return super(Products, self).create(vals)
    