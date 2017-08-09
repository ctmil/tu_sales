# -*- coding: utf-8 -*-

from openerp import tools, models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
import time
from openerp.fields import Date as newdate
from datetime import datetime,date,timedelta

class sale_order(models.Model):
        _inherit = 'sale.order'

	@api.model
	def clean_sale_orders(self):
		now_2hours = datetime.today() - timedelta(hours=1)
		orders = self.search([('state','in',['draft','sent'])])
		for order in orders:
			if order.state in ['draft','sent']:
				for line in order.order_line:
					if order.write_date < str(now_2hours) or line.write_date < str(now_2hours):
						#order.action_cancel()
						line.unlink()
				
