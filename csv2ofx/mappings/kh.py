# -*- coding: utf-8 -*-

from __future__ import absolute_import

from operator import itemgetter

mapping = {
    'has_header': True,
    'account': itemgetter('könyvelési számla'),
    'date': itemgetter('könyvelés dátuma'),
    'amount': itemgetter('összeg'),
    'payee': lambda r: r['partner elnevezése'] if r['partner elnevezése'] else 'K&H',
    'currency': itemgetter('összeg devizaneme'),
    'desc': itemgetter('típus'),
    'notes': itemgetter('közlemény'),
}
