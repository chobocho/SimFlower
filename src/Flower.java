package com.chobocho.hflower;

public class Flower {
    private String orderData;
    private String[] mFlowerOrder;

    enum ORDER {
        ORDER_NAME,
        ORDER_PHONE,
        RECEIVER_NAME,
        RECEIVER_PHONE,
        DELIVERY_DATE,
        DELIVERY_TIME,
        RECEIVED_MESSAGE,
        PRESENT_NAME,
        PODDUCT,
        ADRESS
    };


    public Flower() {
        mFlowerOrder = new String[ORDER.ADRESS.ordinal()+1];
    }

    public void init() {
        orderData = "";
        if (mFlowerOrder != null) {
            for (String s : mFlowerOrder) {
                s = "";
            }
        }
    }

    public String getInfo(int idx) {
        return mFlowerOrder[idx];
    }

    public void DoParsing() {
        if (orderData == null) {
            return;
        }
        else if (orderData.indexOf("1. 보내시는분") != -1) {
            parse2();
        } else {
            parse();
        }
    }


    public void parse() {
        int startName = orderData.indexOf("주문자성함");
        int endName = orderData.indexOf("받는분성함");
        if (startName != -1 && endName != -1) {
            String strOrderPerson = orderData.substring(startName + 1, endName);
            System.out.println(strOrderPerson);
            int sName = strOrderPerson.indexOf(":");
            strOrderPerson = strOrderPerson.substring(sName + 1);
            int eName = strOrderPerson.indexOf("/");
            if (eName != -1) {
                mFlowerOrder[ORDER.ORDER_NAME.ordinal()] = strOrderPerson.substring(0, eName).trim();
                String strOrderPhone = strOrderPerson.substring(eName + 1);
                int endPhone = strOrderPhone.indexOf("/");
                if (endPhone != -1) {
                    mFlowerOrder[ORDER.ORDER_PHONE.ordinal()] = strOrderPhone.substring(0, endPhone).trim();
                } else {
                    mFlowerOrder[ORDER.ORDER_PHONE.ordinal()] = strOrderPhone.trim();
                }
            } else {
                mFlowerOrder[ORDER.ORDER_NAME.ordinal()] = strOrderPerson.trim();
            }
        }

        int startDate = orderData.indexOf("배송날짜");
        if (endName != -1 && startDate != -1) {
            String strReceivePerson = orderData.substring(endName + 1, startDate);
            System.out.println(strReceivePerson);

            int sName = strReceivePerson.indexOf(":");
            strReceivePerson = strReceivePerson.substring(sName + 1);
            int eName = strReceivePerson.indexOf("/");
            if (eName != -1) {
                mFlowerOrder[ORDER.RECEIVER_NAME.ordinal()] = strReceivePerson.substring(0, eName).trim();
                String strOrderPhone = strReceivePerson.substring(eName + 1);
                int endPhone = strOrderPhone.indexOf("/");
                if (endPhone != -1) {
                    mFlowerOrder[ORDER.RECEIVER_PHONE.ordinal()] = strOrderPhone.substring(0, endPhone).trim();
                } else {
                    mFlowerOrder[ORDER.RECEIVER_PHONE.ordinal()] = strOrderPhone.trim();
                }
            } else {
                mFlowerOrder[ORDER.RECEIVER_NAME.ordinal()] = strReceivePerson.trim();
            }
        }


        int startMessage = orderData.indexOf("경조메시지");
        if (startDate != -1 && startMessage != -1) {
            String strReceiveDate = orderData.substring(startDate + 1, startMessage);
            System.out.println(strReceiveDate);

            int sDate = strReceiveDate.indexOf(":");
            strReceiveDate = strReceiveDate.substring(sDate + 1);
            int endDate = strReceiveDate.indexOf("일");
            if (endDate != -1) {
                mFlowerOrder[ORDER.DELIVERY_DATE.ordinal()] = strReceiveDate.substring(0, endDate + 1).trim();
                String strReceiveTime = strReceiveDate.substring(endDate + 1);
                int endTime = strReceiveTime.indexOf("분");
                if (endTime != -1) {
                    int strSlash = strReceiveTime.indexOf('/');
                    int startRecvTime = 0;
                    if (strSlash != -1 && strSlash < endTime) {
                        startRecvTime = strSlash + 1;
                    }
                    mFlowerOrder[ORDER.DELIVERY_TIME.ordinal()] = strReceiveTime.substring(startRecvTime, endTime + 1).trim();
                } else {
                    mFlowerOrder[ORDER.DELIVERY_TIME.ordinal()] = strReceiveTime.trim();
                }
            } else {
                mFlowerOrder[ORDER.DELIVERY_DATE.ordinal()] = strReceiveDate.trim();
            }
        }

        int startOrderPerson = orderData.indexOf("보내는분");
        if (startMessage != -1 && startOrderPerson != -1) {
            String strRecvMessage = orderData.substring(startMessage + 1, startOrderPerson);
            System.out.println(strRecvMessage);

            int sRecvMsg = strRecvMessage.indexOf(":");
            strRecvMessage = strRecvMessage.substring(sRecvMsg + 1);
            int endRecvMsg = strRecvMessage.indexOf("/");
            if (endRecvMsg != -1) {
                mFlowerOrder[ORDER.RECEIVED_MESSAGE.ordinal()] = strRecvMessage.substring(0, endRecvMsg).trim();
            } else {
                mFlowerOrder[ORDER.RECEIVED_MESSAGE.ordinal()] = strRecvMessage.trim();
            }
        }

        int startProduct = orderData.indexOf("제품선택");
        if (startOrderPerson != -1 && startProduct != -1) {
            String strPresentName = orderData.substring(startOrderPerson + 1, startProduct);
            System.out.println(strPresentName);

            int sPresentName = strPresentName.indexOf(":");
            strPresentName = strPresentName.substring(sPresentName + 1);
            int endRecvMsg = strPresentName.indexOf("/");
            if (endRecvMsg != -1) {
                mFlowerOrder[ORDER.PRESENT_NAME.ordinal()] = strPresentName.substring(0, endRecvMsg).trim();
            } else {
                mFlowerOrder[ORDER.PRESENT_NAME.ordinal()] = strPresentName.trim();
            }
        }

        int endProduct = orderData.substring(startProduct+1).indexOf("]");
        if (startProduct != -1 && endProduct != -1) {
            String strProdcut = orderData.substring(startProduct + 1).substring(0,endProduct + 1);
            System.out.println(strProdcut);

            int sPresentName = strProdcut.indexOf(":");
            strProdcut = strProdcut.substring(sPresentName + 1);
            int endRecvMsg = strProdcut.indexOf("/");
            if (endRecvMsg != -1) {
                mFlowerOrder[ORDER.PODDUCT.ordinal()] = strProdcut.substring(0, endRecvMsg).trim();
            } else {
                mFlowerOrder[ORDER.PODDUCT.ordinal()] = strProdcut.trim();
            }
        }

        if (endProduct != -1) {
            String strAddress = orderData.substring(startProduct + 1).substring(endProduct + 1);
            System.out.println(strAddress);

            mFlowerOrder[ORDER.ADRESS.ordinal()] = strAddress.trim();
        }
    }

    public void parse2() {
        int startName = orderData.indexOf("보내시는분");
        int endName = orderData.indexOf("받는분");
        if (startName != -1 && endName != -1) {
            String strOrderPerson = orderData.substring(startName + 1, endName);
            System.out.println(strOrderPerson);
            int sName = strOrderPerson.indexOf(">");
            strOrderPerson = strOrderPerson.substring(sName + 1);
            int eName = strOrderPerson.indexOf("/");
            if (eName != -1) {
                mFlowerOrder[ORDER.ORDER_NAME.ordinal()] = strOrderPerson.substring(0, eName).trim();
                String strOrderPhone = strOrderPerson.substring(eName + 1);
                int endPhone = strOrderPhone.indexOf("2.");
                if (endPhone != -1) {
                    mFlowerOrder[ORDER.ORDER_PHONE.ordinal()] = strOrderPhone.substring(0, endPhone).trim();
                } else {
                    mFlowerOrder[ORDER.ORDER_PHONE.ordinal()] = strOrderPhone.trim();
                }
            } else {
                mFlowerOrder[ORDER.ORDER_NAME.ordinal()] = strOrderPerson.trim();
            }
        }

        int startDate = orderData.indexOf("배송날짜");
        if (endName != -1 && startDate != -1) {
            String strReceivePerson = orderData.substring(endName + 1, startDate);
            System.out.println(strReceivePerson);

            int sName = strReceivePerson.indexOf(">");
            strReceivePerson = strReceivePerson.substring(sName + 1);
            int eName = strReceivePerson.indexOf("/");
            if (eName != -1) {
                mFlowerOrder[ORDER.RECEIVER_NAME.ordinal()] = strReceivePerson.substring(0, eName).trim();
                String strOrderPhone = strReceivePerson.substring(eName + 1);
                int endPhone = strOrderPhone.indexOf("3.");
                if (endPhone != -1) {
                    mFlowerOrder[ORDER.RECEIVER_PHONE.ordinal()] = strOrderPhone.substring(0, endPhone).trim();
                } else {
                    mFlowerOrder[ORDER.RECEIVER_PHONE.ordinal()] = strOrderPhone.trim();
                }
            } else {
                mFlowerOrder[ORDER.RECEIVER_NAME.ordinal()] = strReceivePerson.trim();
            }
        }


        int startMessage = orderData.indexOf("4. 리본");
        if (startDate != -1 && startMessage != -1) {
            String strReceiveDate = orderData.substring(startDate + 1, startMessage);
            System.out.println(strReceiveDate);

            int sDate = strReceiveDate.indexOf("시간");
            strReceiveDate = strReceiveDate.substring(sDate + 2).trim();
            int endDate = strReceiveDate.indexOf("일");
            if (endDate != -1) {
                mFlowerOrder[ORDER.DELIVERY_DATE.ordinal()] = strReceiveDate.substring(0, endDate + 1).trim();
                String strReceiveTime = strReceiveDate.substring(endDate + 1);
                int endTime = strReceiveTime.indexOf("분");
                if (endTime != -1) {
                    mFlowerOrder[ORDER.DELIVERY_TIME.ordinal()] = strReceiveTime.substring(0, endTime + 1).trim();
                } else {
                    mFlowerOrder[ORDER.DELIVERY_TIME.ordinal()] = strReceiveTime.trim();
                }
            } else {
                mFlowerOrder[ORDER.DELIVERY_DATE.ordinal()] = strReceiveDate.trim();
            }
        }

        int startOrderPerson = orderData.indexOf("5. 리본");
        if (startMessage != -1 && startOrderPerson != -1) {
            String strRecvMessage = orderData.substring(startMessage + 1, startOrderPerson);
            System.out.println(strRecvMessage);

            int sRecvMsg = strRecvMessage.indexOf("경조메세지");
            strRecvMessage = strRecvMessage.substring(sRecvMsg + 5);
            int endRecvMsg = strRecvMessage.indexOf("5.");
            if (endRecvMsg != -1) {
                mFlowerOrder[ORDER.RECEIVED_MESSAGE.ordinal()] = strRecvMessage.substring(0, endRecvMsg).trim();
            } else {
                mFlowerOrder[ORDER.RECEIVED_MESSAGE.ordinal()] = strRecvMessage.trim();
            }
        }

        int startAddress = orderData.indexOf("배송지주소");
        if (startOrderPerson != -1 && startAddress != -1) {
            String strPresentName = orderData.substring(startOrderPerson + 1, startAddress);
            System.out.println(strPresentName);

            int sPresentName = strPresentName.indexOf("보내시는분 문구");
            strPresentName = strPresentName.substring(sPresentName + 8);
            int endRecvMsg = strPresentName.indexOf("6.");
            if (endRecvMsg != -1) {
                mFlowerOrder[ORDER.PRESENT_NAME.ordinal()] = strPresentName.substring(0, endRecvMsg).trim();
            } else {
                mFlowerOrder[ORDER.PRESENT_NAME.ordinal()] = strPresentName.trim();
            }
        }

        if (startAddress != -1) {
            String strAddress = orderData.substring(startAddress);
            System.out.println(strAddress);

            int sPresentName = strAddress.indexOf("배송지주소");
            strAddress = strAddress.substring(sPresentName + 5);
            mFlowerOrder[ORDER.ADRESS.ordinal()] = strAddress.trim();
        }
    }

    public void setText(String order) {
            this.orderData= order;
    }


}
