# Description #

Insecure cipher suites being enabled on the server is a classic SSL misconfiguration.
Because the crypto algorithms used with those cipher suites are weak, if those cipher suites were to be negotiated between a client and the server, an attacker could brute force the keys used to encrypt the SSL traffic.
Additionally, SSLv2 itself is broken as a protocol, and allows for cryptographic downgrade attacks.

# Detection #
SSLyze can scan the server in order to detect which cipher suites it supports within the SSL 2.0 , SSL 3.0, TLS 1.0, TLS 1.1 and TLS 1.2 protocols.

` $ python sslyze.py --sslv2 --sslv3 --tlsv1 www.server.com:443 `

![http://sslyze.googlecode.com/svn/wiki/images/weakciphers.png](http://sslyze.googlecode.com/svn/wiki/images/weakciphers.png)

![http://sslyze.googlecode.com/svn/wiki/images/sslv2.png](http://sslyze.googlecode.com/svn/wiki/images/sslv2.png)


# Recommendations #

A properly hardened server should NOT accept the following cipher suites:
  * Any cipher suite that has a key size smaller than 128 bits.
  * Any anonymous cipher suite, because they don't provide server authentication. SSLyze will flag them as "Anon".
  * Any cipher suite that is part of the SSLv2 protocol, because the protocol itself is broken.