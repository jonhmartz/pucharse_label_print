from odoo import models, fields

class PrintLabelWizard(models.TransientModel):
    _name = 'print.label.wizard'
    _description = 'Asistente para imprimir etiquetas'

    purchase_id = fields.Many2one('pucharse.order', string='Orden de Compra')

    def print_labels(self):
        return self.env.ref('pucharse_label_print.report_pucharse_labels').report_action(self.pucharse_id)
