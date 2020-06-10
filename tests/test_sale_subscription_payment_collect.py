# The COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.
import unittest
import doctest

from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import doctest_teardown
from trytond.tests.test_tryton import doctest_checker


class SaleSubscriptionPaymentCollectTestCase(ModuleTestCase):
    'SaleSubscriptionPaymentCollectTestCase'
    module = 'sale_subscription_payment_collect'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            SaleSubscriptionPaymentCollectTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_sale_subscription_payment_collect.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
