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
    netto = fields.Integer(string='Netto', default=100)
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
            ('revoked', 'Dibatalkan')
        ], string='Status PIRT')
    pirt_no = fields.Char(string='No. PIRT')
    pirt_file = fields.Binary(string='File PIRT', attachment=True)
    halal_status = fields.Selection([('not_needed', 'Tidak Memerlukan'),
            ('potential_not_have', 'Belum Memiliki'),
            ('potential_progress', 'Proses Pembuatan'),
            ('owned', 'Memiliki'),
            ('owned_created', 'Dibuat oleh Tim'),
            ('revoked', 'Dibatalkan')
        ], string='Status Halal')
    halal_no = fields.Char(string='No. Halal')
    halal_file = fields.Binary(string='File Halal', attachment=True)
    bpom_status = fields.Selection([('not_needed', 'Tidak Memerlukan'),
            ('potential_not_have', 'Belum Memiliki'),
            ('potential_progress', 'Proses Pembuatan'),
            ('owned', 'Memiliki'),
            ('owned_created', 'Dibuat oleh Tim'),
            ('revoked', 'Dibatalkan')
        ], string='Status BPOM')
    bpom_no = fields.Char(string='No. BPOM')
    bpom_file = fields.Binary(string='File BPOM', attachment=True)
    packaging_ids = fields.One2many('umkm.packaging', 'product_id', string='Packaging')
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

    # Computed fields for certificate icon styling
    show_certificates = fields.Boolean(
        string='Show Certificates',
        compute='_compute_show_certificates'
    )

    pirt_icon_color = fields.Selection([
        ('grey', 'Grey'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('none', 'None')
    ], string='PIRT Icon Color', compute='_compute_certificate_icon_colors')

    halal_icon_color = fields.Selection([
        ('grey', 'Grey'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('none', 'None')
    ], string='Halal Icon Color', compute='_compute_certificate_icon_colors')

    bpom_icon_color = fields.Selection([
        ('grey', 'Grey'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('none', 'None')
    ], string='BPOM Icon Color', compute='_compute_certificate_icon_colors')

    pirt_tooltip = fields.Char(
        string='PIRT Tooltip',
        compute='_compute_certificate_tooltips'
    )

    halal_tooltip = fields.Char(
        string='Halal Tooltip',
        compute='_compute_certificate_tooltips'
    )

    bpom_tooltip = fields.Char(
        string='BPOM Tooltip',
        compute='_compute_certificate_tooltips'
    )

    @api.depends('_type')
    def _compute_show_certificates(self):
        for record in self:
            record.show_certificates = record._type == 'makanan_kemasan'

    @api.depends('pirt_status', 'halal_status', 'bpom_status')
    def _compute_certificate_icon_colors(self):
        for record in self:
            # PIRT color mapping
            if record.pirt_status in ['owned', 'owned_created']:
                record.pirt_icon_color = 'green'
            elif record.pirt_status == 'potential_progress':
                record.pirt_icon_color = 'yellow'
            elif record.pirt_status == 'potential_not_have':
                record.pirt_icon_color = 'grey'
            else:
                record.pirt_icon_color = 'none'

            # Halal color mapping
            if record.halal_status in ['owned', 'owned_created']:
                record.halal_icon_color = 'green'
            elif record.halal_status == 'potential_progress':
                record.halal_icon_color = 'yellow'
            elif record.halal_status == 'potential_not_have':
                record.halal_icon_color = 'grey'
            else:
                record.halal_icon_color = 'none'

            # BPOM color mapping
            if record.bpom_status in ['owned', 'owned_created']:
                record.bpom_icon_color = 'green'
            elif record.bpom_status == 'potential_progress':
                record.bpom_icon_color = 'yellow'
            elif record.bpom_status == 'potential_not_have':
                record.bpom_icon_color = 'grey'
            else:
                record.bpom_icon_color = 'none'

    @api.depends('pirt_status', 'halal_status', 'bpom_status')
    def _compute_certificate_tooltips(self):
        for record in self:
            # PIRT tooltip
            if record.pirt_status == 'owned':
                record.pirt_tooltip = 'PIRT: Memiliki (Punya sertifikat PIRT)'
            elif record.pirt_status == 'owned_created':
                record.pirt_tooltip = 'PIRT: Dibuat oleh Tim (Sertifikat dibuat tim kami)'
            elif record.pirt_status == 'potential_progress':
                record.pirt_tooltip = 'PIRT: Proses Pembuatan (Sedang dalam proses pembuatan)'
            elif record.pirt_status == 'potential_not_have':
                record.pirt_tooltip = 'PIRT: Belum Memiliki (Belum punya sertifikat)'
            else:
                record.pirt_tooltip = 'PIRT: Sertifikat PIRT'

            # Halal tooltip
            if record.halal_status == 'owned':
                record.halal_tooltip = 'Halal: Memiliki (Punya sertifikat Halal)'
            elif record.halal_status == 'owned_created':
                record.halal_tooltip = 'Halal: Dibuat oleh Tim (Sertifikat dibuat tim kami)'
            elif record.halal_status == 'potential_progress':
                record.halal_tooltip = 'Halal: Proses Pembuatan (Sedang dalam proses pembuatan)'
            elif record.halal_status == 'potential_not_have':
                record.halal_tooltip = 'Halal: Belum Memiliki (Belum punya sertifikat)'
            else:
                record.halal_tooltip = 'Halal: Sertifikat Halal'

            # BPOM tooltip
            if record.bpom_status == 'owned':
                record.bpom_tooltip = 'BPOM: Memiliki (Punya sertifikat BPOM)'
            elif record.bpom_status == 'owned_created':
                record.bpom_tooltip = 'BPOM: Dibuat oleh Tim (Sertifikat dibuat tim kami)'
            elif record.bpom_status == 'potential_progress':
                record.bpom_tooltip = 'BPOM: Proses Pembuatan (Sedang dalam proses pembuatan)'
            elif record.bpom_status == 'potential_not_have':
                record.bpom_tooltip = 'BPOM: Belum Memiliki (Belum punya sertifikat)'
            else:
                record.bpom_tooltip = 'BPOM: Sertifikat BPOM'

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
    