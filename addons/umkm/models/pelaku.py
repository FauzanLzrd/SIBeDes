from odoo import models, fields

class PelakuUmkm(models.Model):
    _name = 'umkm.pelaku'
    _description = 'UMKM'
    _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Nama', required=True, tracking=True)
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
    phone = fields.Char(string='Phone', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    ktp_file = fields.Binary(string='File KTP', attachment=True, tracking=True)
    nik = fields.Char(string='NIK', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    image = fields.Binary(string='Foto', attachment=True, tracking=True)

    def action_open_whatsapp(self):
        self.ensure_one()
        if self.phone:
            # Clean phone number: remove spaces, dashes, and ensure no leading +
            phone = self.phone.strip().replace(' ', '').replace('-', '').lstrip('+')
            url = f"https://wa.me/{phone}"
            return {
                'type': 'ir.actions.act_url',
                'url': url,
                'target': 'new',
            }
        else:
            # Maybe show a warning if no phone
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'No Phone Number',
                    'message': 'This contact has no phone number.',
                    'type': 'warning',
                }
            }