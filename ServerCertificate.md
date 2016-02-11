# Description #
For a given server, the SSL certificate it uses can be invalid for various reasons. An invalid certificate greatly threatens the security of any SSL connection to the server, because the server is not properly authenticated.
For example, when the client is a browser, an invalid certificate usually triggers a security warning in the browser, which forces the user to accept the warning in order to actually connect to the server. This means that a network attacker could easily masquerade as the server and provide its own, self-signed certificate to the client, causing the same security warning to be displayed to the user. It makes it difficult for users to know that they're under attack.



# Detection #

SSLyze can verify the server's certificate validity against Mozilla's trusted root store, and print relevant fields of the certificate.

`$ python sslyze.py --certinfo=basic www.server.com:443`

![http://sslyze.googlecode.com/svn/wiki/images/certinfo.png](http://sslyze.googlecode.com/svn/wiki/images/certinfo.png)


# Recommendations #
Here is a non exhaustive list of recommendations regarding the validity of the server's certificate:
  * The subject CN within the certificate should match the server's hostname.
  * The certificate should not be expired.
  * Key size should be 2048 bits or larger.
  * The signature algorithm should not be MD5 or MD2.

# Additional Options #
  * `--certinfo=full` Prints the full certificate.
  * `--certinfo=serial` Prints the serial number.
  * `--certinfo=keysize` Prints the key size.
  * `--certinfo=cn` Prints the Common Name field.