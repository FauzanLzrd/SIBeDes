from odoo import models

class WhatsappMixin(models.AbstractModel):
    _name = 'whatsapp.mixin'
    _description = 'Mixin for WhatsApp functionality'

    def action_open_whatsapp(self):
        self.ensure_one()
        phone_field = getattr(self, 'phone', None)
        if phone_field:
            # Clean phone number: remove spaces, dashes, and ensure no leading +
            phone = phone_field.strip().replace(' ', '').replace('-', '').lstrip('+')
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