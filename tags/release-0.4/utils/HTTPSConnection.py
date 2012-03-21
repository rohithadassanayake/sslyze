#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:         HTTPSConnection.py
# Purpose:      Similar to httplib.HTTPSConnection but uses ctSSL instead of 
#               the standard ssl module. Should eventually be part of ctSSL.
#
# Author:       alban
#
# Copyright:    2011 SSLyze developers (http://code.google.com/sslyze)
#
#   SSLyze is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 2 of the License, or
#   (at your option) any later version.
#
#   SSLyze is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with SSLyze.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

import socket
from httplib import HTTPConnection, HTTPS_PORT

from ctSSL import SSL, SSL_CTX
from ctSSL import constants

from CtSSLHelper import filter_handshake_exceptions
from SSLSocket import SSLSocket

# Create a ctSSL-based HTTPSConnection
class HTTPSConnection(HTTPConnection):
    """
    This class mirrors httplib.HTTPSConnection but uses ctSSL instead of the 
    standard ssl module.
    For now the way to access low level SSL functions associated with a given 
    HTTPSConnection is too just access the ssl and ssl_ctx attribute of the 
    object.
    """
    
    default_port = HTTPS_PORT
    
    def __init__(self, host, port=None, ssl=None, ssl_ctx=None, 
                 strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        
        HTTPConnection.__init__(self, host, port, strict, timeout)

        self.ssl_ctx = ssl_ctx
        self.ssl = ssl
        
        if self.ssl_ctx is None:
            self.ssl_ctx = SSL_CTX.SSL_CTX()
            # Can't verify certs by default
            self.ssl_ctx.set_verify(constants.SSL_VERIFY_NONE)
    
        if self.ssl is None: 
            self.ssl = SSL.SSL(self.ssl_ctx)
            
    
    def connect(self):
        "Connect to a host on a given (SSL) port."
    
        sock = socket.create_connection((self.host, self.port),
                                        self.timeout)
        
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
              
        # Doing something similar to ssl.wrap_socket() but with ctSSL
        self.ssl.set_socket(sock)
        ssl_sock = SSLSocket(self.ssl)
        
        try:
            ssl_sock.do_handshake()
        except Exception as e:
            filter_handshake_exceptions(e)
            
        self.sock = ssl_sock
        
