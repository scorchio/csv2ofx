# -*- coding: utf-8 -*-

from __future__ import absolute_import

from operator import itemgetter

mapping = {
    'has_header': True,
    'delimiter': '\t',
    'account': itemgetter('könyvelési számla'),
    'date': itemgetter('könyvelés dátuma'),
    'amount': itemgetter('összeg'),
    'payee': itemgetter('partner elnevezése'),
    'currency': itemgetter('összeg devizaneme'),
    'desc': itemgetter('típus'),
    'notes': itemgetter('közlemény'),
}
