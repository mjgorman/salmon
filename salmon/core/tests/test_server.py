from django.conf import settings
from django.test.utils import override_settings
from django.utils import unittest
from salmon.core.server import SalmonHTTPServer

class HTTPServiceTest(unittest.TestCase):
    def test_options(self):
        cls = SalmonHTTPServer

        options = {
            'bind': '1.1.1.1:80',
            'accesslog': '/tmp/access.log',
            'errorlog': '/tmp/error.log',
            'timeout': 69,
            'proc_name': 'testicorn',
            'secure_scheme_headers': {},
            'loglevel': 'info',
        }
        with override_settings(WEB_OPTIONS=options):
            server = cls()
            assert server.options['bind'] == '1.1.1.1:80'
            assert server.options['accesslog'] == '/tmp/access.log'
            assert server.options['errorlog'] == '/tmp/error.log'
            assert server.options['timeout'] == 69
            assert server.options['proc_name'] == 'testicorn'
            assert server.options['loglevel'] == 'info'
