class FlowerParser2:
    def __init__(self): 
        print("FlowerParser2")

    def parse(self, orderData):
        result = [""] * 10
 
        startName = orderData.find("보내시는분")
        endName = orderData.find("받는분")
        if (startName != -1 and endName != -1):
            strOrderPerson = orderData[startName + 1:endName]
            print(strOrderPerson)
            sName = strOrderPerson.find(">")
            strOrderPerson = strOrderPerson[sName + 1:]
            eName = strOrderPerson.find("/")
            if (eName != -1):
                result[0] = strOrderPerson[:eName].strip()
                strOrderPhone = strOrderPerson[eName + 1:]
                endPhone = strOrderPhone.find("2.")
                if (endPhone != -1):
                    result[1] = strOrderPhone[:endPhone].strip()
                else:
                    result[1] = strOrderPhone.strip()
            else:
                result[0] = strOrderPerson.strip()

        startDate = orderData.find("배송날짜")
        if (endName != -1 and startDate != -1):
            strReceivePerson = orderData[endName + 1:startDate]
            print(strReceivePerson)

            sName = strReceivePerson.find(">")
            strReceivePerson = strReceivePerson[sName + 1:]
            eName = strReceivePerson.find("/")
            if (eName != -1):
                result[2] = strReceivePerson[:eName].strip()
                strOrderPhone = strReceivePerson[eName + 1:]
                endPhone = strOrderPhone.find("3.")
                if (endPhone != -1):
                    result[3] = strOrderPhone[:endPhone].strip()
                else:
                    result[3] = strOrderPhone.strip()
            else:
                result[2] = strReceivePerson.strip()

        startMessage = orderData.find("4. 리본")
        if (startDate != -1 and startMessage != -1):
            strReceiveDate = orderData[startDate + 1:startMessage]
            print(strReceiveDate)

            sDate = strReceiveDate.find("시간")
            strReceiveDate = strReceiveDate[sDate + 2:].strip()
            endDate = strReceiveDate.find("일")
            if (endDate != -1):
                result[4] = strReceiveDate[:endDate + 1].strip()
                strReceiveTime = strReceiveDate[endDate + 1:]
                endTime = strReceiveTime.find("분")
                if (endTime != -1):
                    result[5] = strReceiveTime[:endTime + 1].strip()
                else:
                    result[5] = strReceiveTime.strip()
                
            else:
                result[4] = strReceiveDate.strip()
            
        

        startOrderPerson = orderData.find("5. 리본")
        if (startMessage != -1 and startOrderPerson != -1):
            strRecvMessage = orderData[startMessage + 1:startOrderPerson]
            print(strRecvMessage)

            sRecvMsg = strRecvMessage.find("경조메세지")
            strRecvMessage = strRecvMessage[sRecvMsg + 5:]
            endRecvMsg = strRecvMessage.find("5.")
            if (endRecvMsg != -1):
                result[6] = strRecvMessage[:endRecvMsg].strip()
            else:
                result[6] = strRecvMessage.strip()
            
        

        startAddress = orderData.find("배송지주소")
        if (startOrderPerson != -1 and startAddress != -1):
            strPresentName = orderData[startOrderPerson + 1:startAddress]
            print(strPresentName)

            sPresentName = strPresentName.find("보내시는분 문구")
            strPresentName = strPresentName[sPresentName + 8:]
            endRecvMsg = strPresentName.find("6.")
            if (endRecvMsg != -1):
                result[7] = strPresentName[:endRecvMsg].strip()
            else:
                result[7] = strPresentName.strip()

        if (startAddress != -1):
            strAddress = orderData[startAddress:]
            print(strAddress)

            sPresentName = strAddress.find("배송지주소")
            strAddress = strAddress[sPresentName + 5:]
            result[9] = strAddress.strip()
        

        return result