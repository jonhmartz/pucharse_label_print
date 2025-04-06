from odoo import models, fields

class PrintLabelWizard(models.TransientModel):
    _name = 'print.label.wizard'
    _description = 'Asistente para imprimir etiquetas'

    purchase_id = fields.Many2one('purchase.order', string='Orden de Compra')

    def print_labels(self):
        return self.env.ref('purchase_label_print.report_purchase_labels').report_action(self.purchase_id)
