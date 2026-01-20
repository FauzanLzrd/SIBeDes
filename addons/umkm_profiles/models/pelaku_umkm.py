from odoo import models, fields

class PelakuUmkm(models.Model):
    _name = 'umkm.pelaku'
    _description = 'Pelaku UMKM'
    _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Nama', required=True, tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    nik = fields.Char(string='NIK', tracking=True)
    ktp_file = fields.Binary(string='File KTP', attachment=True, tracking=True)
    image = fields.Binary(string='Foto', attachment=True, tracking=True)