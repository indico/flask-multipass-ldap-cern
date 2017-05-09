# This file is part of Flask-Multipass-LDAP-CERN.
# Copyright (C) 2017 CERN
#
# Flask-Multipass-LDAP-CERN is free software; you can redistribute it
# and/or modify it under the terms of the Revised BSD License.

from __future__ import unicode_literals

from setuptools import setup


long_description = '''
This package provides the ``ldap_cern`` and ``oauth_cern`` auth providers
and the ``ldap_cern`` identity provider.

These providers are only useful if you are at CERN and intend to use
Flask-Multipass with the CERN authentication infrastructure (LDAP, OAuth
or Shibboleth).
'''.strip()


setup(
    name='Flask-Multipass-LDAP-CERN',
    version='1.0.2',
    url='https://github.com/indico/flask-multipass-ldap-cern',
    license='BSD',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    description='CERN-specific Flask-Multipass providers',
    long_description=long_description,
    py_modules=('flask_multipass_ldap_cern',),
    zip_safe=False,
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
