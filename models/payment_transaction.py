# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class TxConekta(models.Model):
    _inherit = 'payment.transaction'

    conekta_token = fields.Char(string='Token')
