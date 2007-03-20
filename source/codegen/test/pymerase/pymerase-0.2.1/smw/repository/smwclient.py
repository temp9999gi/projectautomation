#
# Implements an xml-rpc client with persistent
# connection
#
from xmlrpclib import *
import time

class SMWClientTransport(Transport):
    def __init__(self, verbose = 1):
        self.our_connection = None
        self.verbose = verbose
        self.quit_flag = 0

    def request(self, host, handler, request_body, verbose=0):
        # We can retry connections here?
        print "HERE"
        if self.our_connection == None:
            print "NEW CONN"
            self.our_connection = self.make_connection(host)

        self.send_request(self.our_connection, handler, request_body)
        self.send_host(self.our_connection, host)
        self.send_user_agent(self.our_connection)
        self.our_connection.putheader("Keep-Alive", "300")
        self.our_connection.putheader("Connection", "Keep-alive")
        self.send_content(self.our_connection, request_body)

        response = self.our_connection.getresponse()
        errcode = response.status
        errmsg = response.reason
        headers = response.msg
        print "got headers", headers


        if errcode != 200:
            raise ProtocolError(
                host + handler,
                errcode, errmsg,
                headers
                )

        return self.parse_response(response)

    def parse_response(self, f):
        # read response from input file, and parse it

        if not self.quit_flag:
            p, u = self.getparser()

        while 1:
            # BUG use select
            response = f.read()
            if not response:
                break
            if self.verbose:
                print "body:", repr(response)
            if not self.quit_flag:
                p.feed(response)

        if self.quit_flag:
            f.close()
            return [0]

        # Persistent
        ###f.close()

        p.close()

        return u.close()


class SMWClientTransportPlain(SMWClientTransport):
    def make_connection(self, host):
        import httplib
        print "Client doesn't use SSL"
        return httplib.HTTPConnection(host)

class SMWClientTransportSSL(SMWClientTransport):
    def make_connection(self, host):
        import httplib
        print "Client uses SSL"
        return httplib.HTTPSConnection(host)


class SMWClient(ServerProxy):
    def __init__(self, uri, transport = None):
        if transport == None:
            if uri[:5] == "https":
                transport = SMWClientTransportSSL()
            else:
                transport = SMWClientTransportPlain()
        self.smw_transport = transport
        ServerProxy.__init__(self, uri, transport)

    def __del__(self):
        # Closes the connection
        self.smw_transport.quit_flag = 1
        self.close()


