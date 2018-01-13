from PyIBapi.config import *
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
from ibapi.contract import *


class IbClient(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        print("init...........")

    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        print("Error: ", reqId, " Code: ", errorCode, " Msg: ", errorString)

    def contractDetails(self, reqId:int, contractDetails:ContractDetails):
        print("contractDetails", reqId, "  ==> ", contractDetails)

    def connect(self):
        EClient.connect(self, host=IB_API_HOST, port=IB_API_PORT, clientId=IB_API_CLIENTID_0)
        print("\n IB serverVersion:%s connectionTime:%s" % (self.serverVersion(),
                                                            self.twsConnectionTime()))

    def close(self):
        print("Closing!!!!.......")
        self.disconnect(self)
        self.close()


