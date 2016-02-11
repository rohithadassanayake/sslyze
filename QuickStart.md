

# Installation #
Supported platforms are Windows 7 and Linux, both 32 and 64 bits.

## Linux ##
Prerequisites: Python 2.6 or 2.7 and OpenSSL 0.9.8+. [Package is here](http://code.google.com/p/sslyze/downloads/list).


## Windows ##
Prerequisites: Python 2.6 or 2.7. OpenSSL 1.0.0c is part of the installation package. There is one package for Python 32 bits, and one for Python 64 bits. [Packages are here](http://code.google.com/p/sslyze/downloads/list).

## Other Platforms ##
Other platforms (including Mac OS X) are not officially supported yet, but SSLyze might work anyway.

# Usage #
The following command line should be used:

` $ python sslyze.py [options] www.target1.com www.target2.com:443 etc... `


Several command line options are available. See the other articles within the wiki for more details regarding each options.


## Regular Scan ##
**` $ python sslyze.py --regular www.target1.com`**

This is what you'll want to use most of the time. It performs a regular HTTP scan. It's a shortcut for `--sslv2 --sslv3 --tlsv1 --reneg --resum --certinfo=basic --hide_rejected_ciphers --http_get`.


## Options ##

### OpenSSL Cipher Suites ###
  * **`--sslv2 --sslv3 --tlsv1`**  : Lists the SSL 2.0, 3.0 and TLS 1.0 OpenSSL cipher suites supported by the server.
  * **`--tlsv1_1 --tlsv1_2`**  : Lists the TLS 1.1 and 1.2 OpenSSL cipher suites supported by the server. Requires OpenSSL 1.0.1 or later.
  * **`--http_get`**  : Option - For each cipher suite, sends an HTTP GET request after completing the SSL handshake and returns the HTTP status code.
  * **`--hide_rejected_ciphers`**  : Option - Hides the (usually long) list of cipher suites that were rejected by the server.


### Session Renegotiation ###
  * **`--reneg`**   : Checks whether the server is vulnerable to insecure renegotiation. Requires OpenSSL 0.9.8m or later.


### Session Resumption ###
  * **`--resum`**   : Tests the server for session resumption support, using both session IDs and TLS session tickets (RFC 5077).
  * **`--resum_rate`**   : Estimates the average rate of successful session resumptions by performing 100 session resumptions.

### Server Certificate ###
  * **`--certinfo=basic`**   : Verifies the server's certificate validity against Mozilla's trusted root store, and prints relevant fields of the certificate.

## Additional Options ##

### StartTLS Support ###
  * **`--starttls=STARTTLS`**   : Identifies the target server(s) as a SMTP or an XMPP server(s) and scans the server(s) using StartTLS. `STARTTLS` should be 'smtp' or 'xmpp'.
  * **`--xmpp_to`**   :  Optional setting for STARTTLS XMPP.  `XMPP_TO` should be the hostname to be put in the 'to' attribute of the XMPP stream. Default is the server's hostname.

### Client Certificate Support ###
Configures SSlyze to use a client certificate in case the server performs mutual authentication. The following options are required:
  * **`--cert=CERT`**   : Client certificate filename.
  * **`--certform=CERTFORM`**   : Client certificate format. DER or PEM (default).
  * **`--key=KEY`**   : Client private key filename.
  * **`--keyform=KEYFORM`**   : Client private key format. DER or PEM (default).
  * **`--pass=KEYPASS`**   : Client private key passphrase.

### HTTPS Proxy Support ###
  * **`--https_tunnel=HTTPS_TUNNEL`**   : Sets an HTTP CONNECT proxy to tunnel SSL traffic to the target server(s). `HTTP_TUNNEL` should be 'host:port'. Requires Python 2.7


### Connections Timeout ###
  * **`--timeout=TIMEOUT`**   : Sets the timeout value in seconds used for every socket connection made to the target server(s). It forces SSLyze to wait more (or less) time for the target server to respond. Default value is 5s.