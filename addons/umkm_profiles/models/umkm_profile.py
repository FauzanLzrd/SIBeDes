from odoo import models, fields

class UmkmProfile(models.Model):
    _name = 'umkm.profile'
    _description = 'UMKM Profile'
    _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Nama Usaha', required=True)
    desa = fields.Selection([
        ('suka_rahmat', 'Suka Rahmat'),
        ('suka_damai', 'Suka Damai'),
        ('danau_redan', 'Danau Redan'),
        ('santan_ulu', 'Santan Ulu'),
        ('martadinata', 'Martadinata'),
        ('bukit_pandan_jaya', 'Bukit Pandan Jaya'),
        ('teluk_pandan', 'Teluk Pandan'),
        ('kandolo', 'Kandolo'),
        ('bontang_lestari', 'Bontang Lestari'),
        ('santan_tengah', 'Santan Tengah'),
        ('santan_ilir', 'Santan Ilir'),
    ], string='Asal Desa', required=True)
    address = fields.Text(string='Alamat Lengkap')
    business_type = fields.Selection([
        ('perorangan', 'Perorangan'),
        ('kelompok', 'Kelompok'),
    ], string='Tipe Bisnis', required=True)
    owner_id = fields.Many2one('umkm.pelaku', string='Pemilik')
    phone = fields.Char(string='No. HP')
    email = fields.Char(string='Email')
    description = fields.Text(string='Deskripsi')
    nib_no = fields.Char(string='No. NIB')
    nib_file = fields.Binary(string='File NIB', attachment=True)
    member_ids = fields.Many2many('umkm.pelaku', string='Anggota')
    product_ids = fields.One2many('umkm.products', 'profile_id', string='Produk')
    latitude = fields.Float(string='Latitude')
    longitude = fields.Float(string='Longitude')
    image = fields.Binary(string='Foto', attachment=True)
    officer = fields.Many2one('hr.employee', string='Petugas')