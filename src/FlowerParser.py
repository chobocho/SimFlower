class FlowerParser:
    def __init__(self): 
        print ("FlowerParser")

    def parse(self, orderData):
        result = [""] * 10
 
        startName = orderData.find("주문자성함")
        endName = orderData.find("받는분성함")
        if (startName != -1 and endName != -1):
            strOrderPerson = orderData[startName + 1:endName]
            print(strOrderPerson)
            sName = strOrderPerson.find(":")
            strOrderPerson = strOrderPerson[sName + 1:]
            eName = strOrderPerson.find("/")
            if (eName != -1):
                result[0] = strOrderPerson[:eName].strip()
                strOrderPhone = strOrderPerson[eName + 1:]
                endPhone = strOrderPhone.find("/")
                if (endPhone != -1):
                    result[1] = strOrderPhone[:endPhone].strip()
                else:
                    result[1] = strOrderPhone.strip()
            else:
                result[0] = strOrderPerson.strip()

        startDate = orderData.find("배송날짜")
        if (endName != -1 and startDate != -1):
            strReceivePerson = orderData[endName + 1:startDate]
            print(strReceivePerson);

            sName = strReceivePerson.find(":")
            strReceivePerson = strReceivePerson[sName + 1:]
            eName = strReceivePerson.find("/")
            if (eName != -1):
                result[2] = strReceivePerson[:eName].strip()
                strOrderPhone = strReceivePerson[eName + 1:]
                endPhone = strOrderPhone.find("/")
                if (endPhone != -1):
                    result[3] = strOrderPhone[:endPhone].strip()
                else:
                    result[3] = strOrderPhone.strip()
            else:
                result[2] = strReceivePerson.strip()


        startMessage = orderData.find("경조메시지")
        if (startDate != -1 and startMessage != -1):
            strReceiveDate = orderData[startDate + 1:startMessage]
            print(strReceiveDate)

            sDate = strReceiveDate.find(":")
            strReceiveDate = strReceiveDate[sDate + 1:]
            endDate = strReceiveDate.find("일")
            if (endDate != -1):
                result[4] = strReceiveDate[:endDate + 1].strip()
                strReceiveTime = strReceiveDate[endDate + 1:]
                endTime = strReceiveTime.find("분")
                if (endTime != -1):
                    strSlash = strReceiveTime.find('/')
                    startRecvTime = 0
                    if (strSlash != -1 and strSlash < endTime):
                        startRecvTime = strSlash + 1
                    
                    result[5] = strReceiveTime[startRecvTime:endTime + 1].strip()
                else:
                    result[5] = strReceiveTime.strip()
            else:
                result[4] = strReceiveDate.strip()


        startOrderPerson = orderData.find("보내는분")
        if (startMessage != -1 and startOrderPerson != -1):
            strRecvMessage = orderData[startMessage + 1:startOrderPerson]
            print(strRecvMessage)

            sRecvMsg = strRecvMessage.find(":")
            strRecvMessage = strRecvMessage[sRecvMsg + 1:]
            endRecvMsg = strRecvMessage.find("/")
            if (endRecvMsg != -1):
                result[6] = strRecvMessage[:endRecvMsg].strip()
            else:
                result[6] = strRecvMessage.strip()
  

        startProduct = orderData.find("제품선택")
        if (startOrderPerson != -1 and startProduct != -1):
            strPresentName = orderData[startOrderPerson + 1:startProduct]
            print(strPresentName)

            sPresentName = strPresentName.find(":")
            strPresentName = strPresentName[sPresentName + 1:]
            endRecvMsg = strPresentName.find("/")
            if (endRecvMsg != -1):
                result[7] = strPresentName[:endRecvMsg].strip()
            else:
                result[7] = strPresentName.strip()


        endProduct = orderData[startProduct+1:].find("]")
        if (startProduct != -1 and endProduct != -1):
            strProduct = orderData[startProduct + 1:]
            strProduct = strProduct[0:endProduct + 1]
            print(strProduct)

            sPresentName = strProduct.find(":")
            strProduct = strProduct[sPresentName + 1:]
            endRecvMsg = strProduct.find("/");
            if (endRecvMsg != -1):
                result[8] = strProduct[:endRecvMsg].strip()
            else:
                result[8] = strProduct.strip()


        if (endProduct != -1):
            strAddress = orderData[startProduct + 1:]
            strAddress = strAddress[endProduct + 1:]
            print(strAddress)
            result[9] = strAddress.strip()

        return result