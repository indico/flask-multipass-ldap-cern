# This file is part of Flask-Multipass-LDAP-CERN.
# Copyright (C) 2017 CERN
#
# Flask-Multipass-LDAP-CERN is free software; you can redistribute it
# and/or modify it under the terms of the Revised BSD License.

from __future__ import unicode_literals

from setuptools import setup


setup(
    name='Flask-Multipass-LDAP-CERN',
    version='1.0.2',
    url='https://github.com/indico/flask-multipass-ldap-cern',
    license='BSD',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    py_modules=('flask_multipass_ldap_cern',),
    zip_safe=False,
    platforms='any',
    install_requires=['flask-multipass', 'python-ldap'],
    entry_points={
        'flask_multipass.auth_providers': {
            'ldap_cern = flask_multipass_ldap_cern:CERNLDAPAuthProvider',
            'oauth_cern = flask_multipass_ldap_cern:CERNOAuthAuthProvider'
        },
        'flask_multipass.identity_providers': {
            'ldap_cern = flask_multipass_ldap_cern:CERNLDAPIdentityProvider'
        }
    }
)
