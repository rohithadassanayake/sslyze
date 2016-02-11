# Description #

Session renegotiation is a mechanism within the SSL protocol that allows the client or the server to trigger a new SSL handshake during an ongoing SSL communication.
Renegotiation was initially designed as a mechanism to increase the security of an ongoing SSL channel, by triggering the renewal of the crypto keys used to secure that channel. However, this security measure isn't needed with modern cryptographic algorithms. Additionally, renegotiation can be used by a server to request a client certificate (in order to perform client authentication) when the client tries to access specific, protected resources on the server.


There is a protocol flaw in that mechanism that was found in 2009. This flaw allows a network attacker to inject plaintext at the beginning of a SSL communication. For example the attacker can inject an HTTP request as if they were the victim. Impact solely depends on what the application running on the server does, but regardless of that, it's a breach in the security SSL is expected to provide.


# Detection #


A server is vulnerable to insecure renegotiation if:
  * It honors client-initiated renegotiations.
  * It doesn't support secure renegotiations.

` $ python sslyze.py --reneg www.server.com:443 `

![http://sslyze.googlecode.com/svn/wiki/images/reneg_insecure.png](http://sslyze.googlecode.com/svn/wiki/images/reneg_insecure.png)

# Recommendations #

Insecure renegotiation can be prevented using one of the two following mitigations:
  * Prevent the server from honoring client-initiated session renegotiations.
  * Update the SSL library used by the server to a recent version. A fix making session renegotiation secure was developed at the protocol level (RFC 5746), and was subsequently implemented in all of the mostly used SSL libraries.