# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################



from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import models, fields, api, _
from openerp.tools.translate import _
from openerp import SUPERUSER_ID, api
import openerp.addons.decimal_precision as dp


class account_invoice(models.Model):
    _inherit = "account.invoice"


    @api.multi
    def print_datecs(self):
         wizard = self.env['export.datecs'].with_context({'active_id':self.id}).create({})
         return {
             'type' : 'ir.actions.act_url',
             'url': '/web/binary/saveas?model=export.datecs&field=data_file&id=%s&filename_field=name' % (wizard.id),
             'target': 'self',
             }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
