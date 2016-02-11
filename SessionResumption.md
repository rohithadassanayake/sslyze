# Description #

Session resumption is a performance optimization that allows a client/server pair to re-use previously generated crypto material, so that they don't have to compute new crypto keys every time a connection gets established. Because it greatly reduces the overhead caused by SSL/TLS, it's a crucial server configuration in order to make SSL/TLS affordable.

# Detection #
SSLyze can test the server for session resumption support, using both session IDs and TLS session tickets (RFC 5077).

` $ python sslyze.py --resum www.server.com:443 `

![http://sslyze.googlecode.com/svn/wiki/images/resum.png](http://sslyze.googlecode.com/svn/wiki/images/resum.png)

# Recommendations #
While not a security concern, session resumption should be enabled because of the notable performance optimization it provides.

# Detection when there is a load balancer #

If the domain being tested relies on a load balancer that dispatches incoming connections to multiple servers, "--resum\_rate" should be used as well for a more accurate analysis.

` $ python sslyze.py --resum_rate www.server.com:443 `

![http://sslyze.googlecode.com/svn/wiki/images/resum_rate.png](http://sslyze.googlecode.com/svn/wiki/images/resum_rate.png)

SSLyze will estimate the average rate of successful session resumptions by performing 100 session resumptions.

On large scale websites/domains, a common configuration is to have a load balancer that transparently dispatches incoming client connections to the single domain, to one of the multiple "backend" servers. This can disrupt SSL session resumption because for a given client, only the server that did the initial SSL handshake has the client's SSL session ID and info cached. So if on its next connection, the client gets dispatched to a different server, the client's SSL session cannot be resumed because the new server doesn't know about it.

# Recommendations when there is a load balancer #

For any session resumptions to actually happen, the load balancer has to be properly configured, and it's valuable to estimate the rate at which successful session resumptions happen. While all the servers may individually have session resumption enabled, a load balancer that has not been made aware of session resumption will ruin SSL performance.