#!/usr/bin/env python3

from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, ssl
from twisted.python import log
from OpenSSL import crypto
import sys

log.startLogging(sys.stdout)

path = "/home/tfonda/Documenti/demo/"

resource = File(path + "www/")
factory = Site(resource)

with open(path + 'cert.pem', 'rb') as fp:
    ssl_cert = fp.read()
with open(path + 'key.pem', 'rb') as fp:
    ssl_key = fp.read()

reactor.listenTCP(80, factory)
reactor.listenSSL(443, factory, ssl.CertificateOptions(
    privateKey = crypto.load_privatekey(crypto.FILETYPE_PEM, ssl_key),
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, ssl_cert),
    enableSessions = False,
    insecurelyLowerMinimumTo = ssl.TLSVersion.TLSv1_2,
    lowerMaximumSecurityTo = ssl.TLSVersion.TLSv1_3
    )
)
reactor.run()
