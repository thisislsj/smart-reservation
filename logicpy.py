msg=["02","07","3"]
msgSimple="batman"
print("msg is ",msgSimple)

seatsAvailable=50
referencecode=5

while True:
    msgInput=input("Type the msg: ")
    print(msgInput)

    if msgInput=="superman":
        if seatsAvailable >0:
            referencecode=referencecode+1
            seatsAvailable=seatsAvailable-1
            print(seatsAvailable)
            reply="Your reference code is" , "MON", #referencecode
            print(reply) #replace with send SMS method
            

        else:
            reply="No seats available"
            print(reply) #replace with send SMS method
    else:
        reply="Your request is invalid"
        print(reply)

    
    
    


    
    

