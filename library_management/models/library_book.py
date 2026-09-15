from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
<<<<<<< HEAD
    _description = 'Livre de bibliotheque'

    name = fields.Char(string='Titre', required=True)
    isbn = fields.Char(string='ISBN')
    author_id = fields.Many2one('library.author', string='Auteur')
    publish_date = fields.Date(string='Date de publication')
    available = fields.Boolean(string='Disponible', default=True)
    lost = fields.Boolean(string='Perdu', default=False)
    lost_date = fields.Date(string='Date de perte')
    active = fields.Boolean(default=True)
    loan_ids = fields.One2many('library.loan', 'book_id', string='Emprunts')

    @api.constrains('isbn')
    def _check_isbn(self):
        for record in self:
            if record.isbn and len(record.isbn) not in (10, 13):
                raise ValidationError("L'ISBN doit contenir 10 ou 13 caracteres.")

    def action_archive_lost_books(self):
        from datetime import date, timedelta
        limit_date = date.today() - timedelta(days=180)
        books = self.search([
            ('lost', '=', True),
            ('lost_date', '<=', limit_date),
            ('active', '=', True),
        ])
        books.write({'active': False})
=======
    _description = 'Livre de la bibliotheque'

    name = fields.Char(string='Titre', required=True)
    author = fields.Char(string='Auteur (texte libre)')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date de publication')
    available = fields.Boolean(string='Disponible', default=True)
    author_id = fields.Many2one('library.author', string='Auteur')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('available', 'Disponible'),
        ('borrowed', 'Emprunte'),
        ('lost', 'Perdu'),
    ], string='Etat', default='draft')
    loan_ids = fields.One2many('library.loan', 'book_id', string='Emprunts')
    is_overdue = fields.Boolean(string='En retard', compute='_compute_is_overdue')

    @api.depends('state', 'loan_ids.return_date')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for book in self:
            book.is_overdue = False
            if book.state == 'borrowed':
                for loan in book.loan_ids:
                    if loan.return_date and loan.return_date < today:
                        book.is_overdue = True
                        break

    @api.constrains('isbn')
    def _check_isbn_length(self):
        for book in self:
            if book.isbn and len(book.isbn) != 13:
                raise ValidationError("L'ISBN doit faire exactement 13 caracteres.")

    @api.onchange('author_id')
    def _onchange_author_id(self):
        if self.author_id and not self.name:
            self.name = "Nouveau livre de %s" % self.author_id.name

    def action_borrow(self):
        for book in self:
            book.state = 'borrowed'
            book.available = False
            self.env['library.loan'].create({
                'book_id': book.id,
                'borrow_date': fields.Date.today(),
            })
>>>>>>> 10ec73379cb3bfc326fd7c28c6c8901fbd86c5cf
