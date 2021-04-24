class PingResult:
    def __init__(self, domainName='', errorMsg='', numPacketsTransmitted=-1, numPacketsRecieved=-1, percentPacketLoss=-1, averageRTT=-1 ):
        self.domainName = domainName
        self.errorMsg = errorMsg
        self.numPacketsTransmitted = numPacketsTransmitted
        self.numPacketsRecieved = numPacketsRecieved
        self.percentPacketLoss = percentPacketLoss
        self.averageRTT = averageRTT