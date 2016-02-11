# Description #
THC has released a DOS tool that exploits SSL renegotiation to perform a denial of service on a given SSL server. It uses renegotiation to constantly trigger new SSL handshakes with the server, using one single TCP connection. See http://www.thc.org/thc-ssl-dos/ .
For more information about renegotiation, see InsecureRenegotiation.



# Detection #

The current version of THC's SSL DOS tool requires the server to honor client-initiated renegotiations in order to work.

` $ python sslyze.py --reneg www.server.com:443 `

![http://sslyze.googlecode.com/svn/wiki/images/reneg_thc.png](http://sslyze.googlecode.com/svn/wiki/images/reneg_thc.png)

# Recommendation #
A mitigation against the current version of THC's SSL DOS tool is to prevent the server from honoring client-initiated renegotiations.
However, as explained on their website, "The tool can be modified to work
without SSL-RENEGOTIATION by just establishing a new TCP connection for every
new handshake".