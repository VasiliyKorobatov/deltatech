# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 Deltatech All Rights Reserved
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



from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
import logging


from openerp.addons.product import _common

_logger = logging.getLogger(__name__)

class stock_move(models.Model):
    _inherit = "stock.move"

    def _get_invoice_line_vals(self, cr, uid, move, partner, inv_type, context=None):
        res = super(stock_move, self)._get_invoice_line_vals(cr, uid, move, partner, inv_type, context=context)
        packs = {}
        for quant in move.quant_ids:
            if quant.qty > 0:
                key = str(int(quant.qty))
                if not key in packs:
                    packs[key] = 1
                else:
                    packs[key] +=1
        pack_str = ''
        print packs
        for key in packs:
            pack_str += str(packs[key]) + ' x ' +str(key) + ';'  #+ move.product_uom.name +'; '         
        res['name'] +=  '\n' +  pack_str  
        if inv_type in ('out_invoice', 'out_refund') and move.procurement_id and move.procurement_id.sale_line_id:
            sale_line = move.procurement_id.sale_line_id 
            if sale_line.order_id.client_order_ref:
                str_date = fields.Datetime.from_string(sale_line.order_id.date_order).strftime('%d-%m-%Y')
                
                res['name'] +=  '\n' + _('Ord.') +  sale_line.order_id.client_order_ref + '/'+ str_date
                
                sale_line.order_id.date_order[:10]
        return res
 
class stock_package(models.Model):
    _inherit = "stock.quant.package"
    
    volume = fields.Float('Volume', help="The volume in m3.")
    weight = fields.Float('Gross Weight', digits=dp.get_precision('Stock Weight'), help="The gross weight in Kg.")
    weight_net = fields.Float('Net Weight', digits=dp.get_precision('Stock Weight'), help="The net weight in Kg.")





# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: