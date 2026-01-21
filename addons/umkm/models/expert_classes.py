from odoo import models, fields

class PelakuUmkm(models.Model):
    _name = 'umkm.expert_classes'
    _description = 'Kelas Experts'
    # _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(string='Nama Kelas', required=True)
    lecturer = fields.Char(string='Nama Pemateri', required=True)
    start_date = fields.Date(string='Tanggal Mulai', required=True)
    end_date = fields.Date(string='Tanggal Akhir', required=True)
    materials = fields.One2many(
        comodel_name="ir.attachment",
        inverse_name="res_id",
        string="Materials",
        domain=[("res_model", "=", "umkm.expert_classes")]
    )
    attendances = fields.One2many(
        comodel_name="umkm.expert_attendances",
        inverse_name="expert_class_id",
        string="Kehadiran"
    )
