# 8-Relays-Card-for-Raspberry-Pi
Program for control (or test) Home Automation 8-Layer Stackable Card for Raspberry Pi (8 Relays)

  Read the product information on this site: 
  https://sequentmicrosystems.com/products/raspberry-pi-home-automation-card

  To install the necessary library "libioplus" follow the procedure here:
  https://github.com/SequentMicrosystems/ioplus-rpi/blob/master/python/README.md

  Next functions of the library "libioplus" for control Home Automation 8-Layer 
  Stackable Card for Raspberry Pi (Sequent Microsystems) are presented here:
  https://github.com/SequentMicrosystems/ioplus-rpi/blob/master/python/ioplus/README.md



  This program was created to control (or test) 
  8 relays on Home Automation 8-Layer Stackable Card 
  for Raspberry Pi (Sequent Microsystems)
 
  Functions included:

  - setOneToAll           ...     Set 1 to all Relays with break between each other
  - setRandomThreeRelays  ...     Randomly select 3 relays and set them on 1,
                                  if the relay already has the state 1, 
                                  only print information and do nothing
  - printStateAll         ...     Print state of all relays
  - resetAllToZero        ...     Reset all relays to 0
  - printStateOnlyOne     ...     Return information with state of one specific relay
