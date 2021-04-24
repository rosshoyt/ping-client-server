class PingResult:
    domainName = 'unset'
    error = 'unset'
    numPacketsTransmitted = 0
    numPacketsRecieved = 0
    packetLossPercentage = numPacketsRecieved / numPacketsTransmitted
    averageRTT = 0
