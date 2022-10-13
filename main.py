from  libioplus import setRelayCh, getRelayCh
from time import sleep
from random import randint


#  Read the product information on this site: 
#  https://sequentmicrosystems.com/products/raspberry-pi-home-automation-card

#  To install the necessary library "libioplus" follow the procedure here:
#  https://github.com/SequentMicrosystems/ioplus-rpi/blob/master/python/README.md

#  Next functions of the library "libioplus" for control Home Automation 8-Layer 
#  Stackable Card for Raspberry Pi (Sequent Microsystems) are presented here:
#  https://github.com/SequentMicrosystems/ioplus-rpi/blob/master/python/ioplus/README.md



#  This program was created to control (or test) 
#  8 relays on Home Automation 8-Layer Stackable Card 
#  for Raspberry Pi (Sequent Microsystems)
 
#  Functions included:
#
#  - setOneToAll            ...     Set 1 to all Relays with break between each other
#  - setRandomThreeRelays   ...     Randomly select 3 relays and set them on 1,
#                                   if the relay already has the state 1, 
#                                   only print information and do nothing
#  - printStateAll          ...     Print state of all relays
#  - resetAllToZero         ...     Reset all relays to 0
#  - printStateOnlyOne      ...     Return information with state of one specific relay



time = 0.5   # 0,5 value used by sleep function as break between operations with relays



def setOneToAll():

    # set 1 to all Relays with break between each other

    print("\n\nSet 1 to all Relays:\n-----------------------\n")
    setRelayCh(0,1,1)
    sleep(time)
    printStateOnlyOne(1)
    setRelayCh(0,2,1)
    sleep(time)
    printStateOnlyOne(2)
    setRelayCh(0,3,1)
    sleep(time)
    printStateOnlyOne(3)
    setRelayCh(0,4,1)
    sleep(time)
    printStateOnlyOne(4)
    setRelayCh(0,5,1)
    sleep(time)
    printStateOnlyOne(5)
    setRelayCh(0,6,1)
    sleep(time)
    printStateOnlyOne(6)
    setRelayCh(0,7,1)
    sleep(time)
    printStateOnlyOne(7)
    setRelayCh(0,8,1)
    sleep(time)
    printStateOnlyOne(8)



def setRandomThreeRelays():

    # randomly select 3 relays and set them on 1
    # if the relay already has the state 1, only print information and do nothing

    print("\n\nThese Relays are set on (max 3):\n--------------------------------\n")
    for x in range(3):
        sleep(time)
        relay_number = randint(1,8)
        print("relay ",relay_number," set on 1")   
        relay_state = getRelayCh(0,relay_number)
        if relay_state:
            print(relay_number," already with ",relay_state)
        else:
            setRelayCh(0,relay_number,1) 
    sleep(time)



def printStateAll():

    # print state of all relays

    print("\n\nThe state of all Relays:\n------------------------\n")
    for y in range(1,9):
        sleep(time)
        relay_state_y = getRelayCh(0,y)
        print("relay ",y,": ",relay_state_y)



def printStateOnlyOne(relay_number_single):

    # return information with state of one specific relay

    relay_state_only_one = getRelayCh(0,relay_number_single)
    return print("relay ",relay_number_single,": ",relay_state_only_one)



def resetAllToZero():

    # reset all relays to 0

    print("\n\nSetting all Relays with 1 back to 0:\n------------------------------------\n")
    for i in range(1,9):
        sleep(time)
        relay_state_i = getRelayCh(0,i)
        print("relay ",i,": ",relay_state_i)
        if relay_state_i == 1:
            setRelayCh(0,i,0)
            sleep(time)
            relay_state_i = getRelayCh(0,i)
            print("relay ",i,": ",relay_state_i," - changed back")
    print("\n")




# choosed funtions to show/test

setOneToAll()
resetAllToZero()
setRandomThreeRelays()
printStateAll()
resetAllToZero()
