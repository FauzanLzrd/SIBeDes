from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import ValidationError

class ExpertAttendances(models.Model):
    _name = 'umkm.expert_attendances'
    _description = 'Kehadiran Kelas Experts'
    # _inherit = ["image.mixin", "mail.thread", "mail.activity.mixin"]

    expert_class_id = fields.Many2one('umkm.expert_classes', string='Kelas Expert', required=True)
    pelaku_id = fields.Many2one('umkm.pelaku', string='Pelaku UMKM', required=True)
    attendance = fields.Boolean(string='Kehadiran', default=True)
    assignment = fields.Boolean(string='Tugas', default=False)

    @api.constrains('expert_class_id', 'pelaku_id')
    def _check_unique_attendance(self):
        for record in self:
            existing = self.search([
                ('expert_class_id', '=', record.expert_class_id.id),
                ('pelaku_id', '=', record.pelaku_id.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError('Pelaku memiliki duplikat kehadiran di kelas yang sama.')
