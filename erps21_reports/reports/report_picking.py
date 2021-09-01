from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'report.erps21_reports.erps21.picking.report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)

        return {
            'doc_ids': docids,
            'docs': docs,
        }
