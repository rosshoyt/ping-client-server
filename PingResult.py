class PingResult:
    def __init__(self, domainName='', errorMsg='', numPacketsTransmitted=-1, numPacketsRecieved=-1, percentPacketLoss=-1, averageRTT=-1 ):
        self.domainName = domainName
        self.errorMsg = errorMsg
        self.numPacketsTransmitted = numPacketsTransmitted
        self.numPacketsRecieved = numPacketsRecieved
        self.percentPacketLoss = percentPacketLoss
        self.averageRTT = averageRTT

    def errorOccured(self):
        '''
        Method that returns true if there was an error when pinging.
        True if error message has any length > 0, false otherwise
        '''
        return len(self.errorMsg) > 0