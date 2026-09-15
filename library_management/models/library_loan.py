from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Emprunt de livre'

    book_id = fields.Many2one('library.book', string='Livre', required=True)
    partner_id = fields.Many2one('res.partner', string='Emprunteur')
    borrow_date = fields.Date(string='Date d\'emprunt', default=fields.Date.today)
    return_date = fields.Date(string='Date de retour prevue')