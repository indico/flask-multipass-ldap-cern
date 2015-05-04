Flask-Multipass-LDAP-CERN
-------------------------

This module provides [Flask-Multipass][1] auth/identity providers named `ldap_cern`.
They behave like the default `ldap` providers, but avoid some quirks the data coming
from CERN LDAP has:

- People who log in using Google, Facebook, etc. have no affiliation instead of e.g. 'urn:Facebook'
- People who log in using eduGAIN have their proper affiliation without the 'eduGAIN - ' prefix.

It also sets some default LDAP settings suitable for the CERN LDAP server.

[1]: https://github.com/indico/flask-multipass
