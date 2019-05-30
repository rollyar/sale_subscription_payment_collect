# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['Subscription']


class Subscription(metaclass=PoolMeta):
    __name__ = 'sale.subscription'
    paymode = fields.Many2One('payment.paymode', 'Paymode',
        domain=[('party', '=', Eval('party', None))], depends=['party'])

    def __get_paymode(self):
        '''
        Return paymode.
        '''
        if self.party:
            if self.party.customer_paymode:
                self.paymode = self.party.customer_paymode

    @fields.depends('party', 'paymode')
    def on_change_party(self):
        super(Subscription, self).on_change_party()
        self.paymode = None
        self.__get_paymode()

    def _get_invoice(self):
        invoice = super(Subscription, self)._get_invoice()
        if invoice:
            invoice.paymode = self.paymode
        return invoice
