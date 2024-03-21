def faq(x):
    x=x.lower()
    resp=''

    #Tickets & Fair
    if ('what' in x and 'token' in x):
        resp+='A token is a valid ticket used for single journey travel.'
        
    if ('get' in x or 'purchase' in x or 'buy' in x) and ('token' in x):
        resp+='Tokens are available across all ticketing windows and Ticket Vending Machines at stations.'

    if (('can' in x or 'how' in x) and ('purchase' in x or 'get' in x) and ('token' in x or 'card' in x) and 'paid area' in x):
        resp+='Tokens cant be purchased from the paid area of the station.'
        
    if (('types' in x or 'kind' in x) and ('tokens' in x or 'cards' in x)):
        resp+='''These types of tokens/smart cards are available in Delhi Metro: 
1)  Single Journey Token 
2) Smart Card 
3) Tourist Card (1 day or 3 days) 
4) Single Journey Paper QR Ticket, Mobile App based QR Ticket 
5) Trip Card (10, 30, 45 Trip), Mobile App based Trip Pass'''
        
    if (('time limit' in x and ('enter' in x or 'get in' in x)) or ('how long' in x and 'token' in x and 'valid' in x)):
        resp+='The token remains valid for a whole day'
        
    if (('time limit' in x and ('exit' in x or 'get out' in x)) or ('how long' in x and 'stay' in x and 'destination station' in x)):
        resp+='''The time limit within which you must exist from the destination sation depends on your travelling distance:
1) 0-12 km: 65
2) 12-21 km: 100
3) More than 21 km: 180

After expiry of the time limit, a penalty @ Rs 10/ per hour subject to maximum of Rs 50/- will be charged.
In Airport Express Line - The maximum travel time limit is 65 Minutes for single journey. After expiry of the time limit a penalty @ Rs 20/ per hour subject to maximum of Rs 400/- will be charged.'''
        
    if ('can' in x and ('exit' in x or 'get out' in x) and 'same station' in x):
        resp+='''You have to exit within 20 minutes after entry. After expiry of the time limit a penalty @ Rs10/ per hour subject to maximum of Rs 50/- will be charged.
In Airport Express Line - within 30 minutes after entry. After expiry of the time limit a penalty @ Rs20/ per hour subject to maximum of Rs 400/- will be charged.'''

    if (('can' in x or 'how' in x) and 'return' in x and 'token' in x):
        resp+='You cannot purchase a return token'

    if (('can' in x or 'how' in x) and ('enter' in x or 'get in' in x or 'board' in x) and ('any' in x or 'other' in x)):
        resp+='You have to enter the station from where you purchased the token.'

    if (('how' in x or 'on what basis' in x) and 'fare' in x and 'between' in x):
        resp+='Fare is fixed on the basis of distance between the stations'

    if (('refund' in x or 'return' in x) and ('token' in x or 'ticket' in x)):
        resp+='An unused token is refundable at full amount from token purchase station only, within 60 minutes of purchase of token. Partially used tokens can be refunded in exceptional cases, like disruption in service, unusual delay in train running due to incident/accident. In Airport Express Line - Refund of Single Journey Paper QR ticket is not permitted. Partially used Single Journey Paper QR ticket can be refunded in exceptional cases like disruption in services.'

    if (('extend' in x or 'increase' in x or 'beyond' in x or 'past' in x) and ('original' in x or 'actual' in x or 'destined' in x)):
        resp+='If you are token holder, the additional fare for extended journey has to be paid at customer care centre of destination station before making an exit from AFC gates. If you are a smart card holder, the fare for journey will be automatically deducted at the time of exit.'

    if (('lost' in x or 'lose' in x or 'misplace' in x) and ('token' in x or 'card' in x)):
        resp+='You should approach Customer Care Centre at your destination station. You will be treated without ticket & shall be chargedMax. Fare + Rs 50/-, In case later on passenger approaches that Token/Card is recovered, no refund is permissible & token shall be confiscated.'

    if (('token' in x or 'card' in x) and ('not accepted' in x or 'error' in x or 'not accepting' in x or 'fail' in x)):
        resp+='Contact Customer Care Centre with token/card for assistance.'

    if ('what' in x and 'card' in x):
        resp+='A Smart Card is special type of ticket used for multiple journeys based on value available on it.'

    if (('use' in x or 'advantage' in x) and'card' in x):
        resp+='''The use of smart card offer following advantages:
1) Save time from daily purchase of token
2) Avoid standing in queue for purchase of token
3) Provides freedom of choice of originating and destination station.
4) A discount of 10% will be given on every journey made by the passenger on smart card.'''

    if ('how' in x and 'card' in x and 'work' in x):
        resp+='Smart card is a contactless card. You just place your smart card on the reader of AFC gate; it will automatically validate the card, and deduct the correct fare for the journey taken at the time of exit.'

    if (('how' in x or 'where' in x) and ('purchase' in x or 'buy' in x or 'get' in x) and 'card' in x):
        resp+='Smart Cards can be purchased from Customer Care centre of any Station & from SCVM (Smart Card Vending Machine) available at selected metro stations of DMRC.'

    if (('how' in x or 'can' in x) and ('purchase' in x or 'buy' in x or 'get' in x) and ('card' in x or 'token' in x or 'ticket' in x) and 'online' in x):
        resp+='One can purchase cards/tokens from counter at station only, however facility for online recharge of smart card is available through website www.dmrcsmartcard.com, Paytm, PhonePe etc.'

    if (('submit' in x or 'give' in x or 'provide' in x) and ('document' in x or 'proof' in x or 'id' in x) and 'card' in x):
        resp+='You do not need to provide any documents to purchase a smart card'

    if (('purchase' in x or 'buy' in x or 'get' in x) and ('card' in x or 'token' in x) and ('family' in x or 'friend' in x or 'anyone' in x or 'someone' in x or 'another' in x)):
        resp+='You can buy a smart card for anyone.'

    if (('how many' in x or 'multiple' in x or 'many' in x) and ('single' in x or 'one' in x) and 'card' in x):
        resp+='Only one person is authorised to travel on single smart card at a time.'

    if (('validity' in x or 'how long' in x or 'valid' in x) and 'card' in x):
        resp+='A Smart Card is valid for 10 years from the date of last recharge.'

    if (('discount' in x or 'less' in x) and ('card' in x)):
        resp+='A discount of 10% will be given on every journey made by the passenger on smart card.'

    if (('check' in x or 'know' in x) and ('balance' in x or 'available' in x or 'left' in x) and 'card' in x):
        resp+='The balance available on a Smart Card can be checked at Ticket Reader cum add value machine (AVM) available on Customer Care Centres at a Station.'

    if (('minimum' in x or 'least' in x) and ('balance' in x or 'available' in x or'left' in x) and 'card' in x and ('travel' in x or 'go' in x or 'board' in x or 'enter' in x)):
        resp+='A minimum balance (presently Rs10/-) is required to enter in station. The customer can travel up to his desired destination. The difference in the fare & available balance will be recorded in his card which will be automatically adjusted upon next recharge or from security deposit during refund.'

    if (('precautions' in x or 'take care' in x or 'measures' in x) and 'card' in x):
        resp+='Show your card at the entry gate , every valid entry is to be followed by valid exit. In case of entry/exit mismatch, penalty/surcharge equivalent to highest value transaction among the last five journeys performed will be charged.'

    if (('refund' in x or 'get' in x or 'take' in x) and ('balance' in x or 'available' in x or 'left' in x) and ('from' in x or 'in' in x) and 'card' in x):
        resp+='The balance (excluding security deposit) in smart card shall not be refunded'

    if ('card' in x and ('exit' in x or 'go out' in x or 'leave' in x) and ('same' in x or 'starting' in x or 'initial' in x)):
        resp+='Fare of Rs10/- will be deducted from Smart Card if you entered and exited from the same station.'

    if ('card' in x and ('not working' in x or 'failed' in x)):
        resp+='It is possible that the chip of Smart Card becomes unreadable in the system. In such cases the passenger will be issued a new smart card of Rs.150/- (Rs50/- security deposit and Rs 100/- electronic value) immediately after payment of Rs 100/- if card is not physically damaged.'

    if (('why' in x or 'reason' in x or 'how' in x) and 'card' in x and ('damage' in x or 'handle' in x)):
        resp+='Smart card should be handled with care. Do not expose them to extreme temperature, moister, bend or keep near the magnets.'

    if (('concession' in x or 'discount' in x or 'less' in x or('is' in x and 'fare' in x) or 'token' in x) and ('students' in x or 'senior' in x or 'handicapped' in x or 'women' in x)):
        resp+='No concession is provided to anyone.'

    if (('free' in x or 'criteria' in x or 'discount' in x or ('is' in x and 'fare' in x) or 'token' in x) and ('child' in x or 'infant' in x or 'toddler' in x or 'baby' in x or 'kid' in x)):
        resp+='Children upto 3 feet (90 cms) height are allowed to travel free if accompanied by an adult. For children above 3 feet (90 cms) , normal fare will be charged.'

    if ('monthly' in x):
        resp+='No monthly card is available for DMRC. This facility is available only on Airport Express Line, monthly card having provision of 30 & 45 trips has been made available in Airport Express Line of DMRC exclusively'


    if ('what' in x and 'tourist card' in x):
        resp+='Tourist cards shall be available with unlimited rides based on validity period. 1 day validity tourist card is valid for one day and 3 day validity tourist card is valid for three days from the date of sale.'

    if (('how' in x or 'where' in x) and ('get' in x or 'purchase' in x or 'buy' in x) and 'tourist' in x):
        resp+='A Tourist Card can be purchased from Customer Care Centre of any Station. 1 day validity tourist cards can be purchased for Rs. 200/- and 3 days validity tourist card can be purchased at Rs 500/- out of which security deposit of Rs 50/- is refundable. Tourist Card is only applicable in DMRC network.'

    if (('how many' in x or 'multiple' in x or 'many' in x) and ('journeys' in x or 'trips' in x or 'rides' in x) and 'tourist card' in x):
        resp+='Unlimited rides for the day of purchase on 1 day validity tourist cards and unlimited rides for 3 days on 3 days validity tourist cards.'

    if ('refund' in x and 'tourist' in x):
        resp+='Irrespective of use, only security deposit (Rs 50/-) amount is refunded after depositing the card.'

    if ('what' in x and ('damaged' in x or 'physically' in x or 'destroyed' in x) and 'card' in x):
        resp+='''Smart Card is considered as damaged if:
a) It's in bent condition (when Smart card is placed on flat surface, all the four corners are not touching the surface). Visible mark /crease on Smart Card.
b) It has visible cut mark or corner is cut.
c) It's surface is badly worn out and/or engraved ID is not visible.
d) It's having hole, mark of staple, punched, burnt, laminated with other items, chemically treated, etc.
e) It's broken or any part damaged.'''

    if ('bharat qr code' in x and ('no sms' in x or 'not recieved' in x or 'get' in x)):
        resp+='Service will not be provided to the passenger if the DMRC operator doesnt recieve an SMS. DMRC’s operator will note down the reference number, amount, date & time of transaction and name of passenger to process the refund (If the amount is deducted from passenger account).'


    #Helpline
    if (('know' in x or 'information' in x) and ('delay' in x or 'failure' in x) and ('metro' in x or 'train' in x or 'services' in x)):
        resp+='Contact 24x7 DMRC helpline number: 155370'

    if (('know' in x or 'information' in x) and ('nearest' in x or 'closest' in x)):
        resp+='''
1) You may contact DMRC 24x7 DMRC helpline number.
2) You may visit Tour Guide section of Delhi Metro website
3) Book named'Delhi by Metro'is also recommended, which is available at Patel Chowk metro station on MRP of Rs. 399/-'''


    #Facility at Station and in Train

    if (('assistance' in x or 'help' in x or 'medic' in x) and ('ill' in x or 'sick' in x or 'medical' in x)):
        resp+='Passenger Emergency Alarm/Handle are provided on every alternate door of Metro Train. By operating this, the problem can be informed to Train Operator.Next station will be informed to provide /arrange prompt medical assistance.'

    if ('wheel chair' in x):
        resp+='While entering at station contact Customer Care Centre for assistance. Staff will arrange the wheel chair at entry and exit station or you may also contact 24x7 DMRC Helpline number so that it can be provided on your arrival at station.'

    if (('restroom' in x or 'toilet' in x or 'washroom' in x)):
        resp+='Toilet facility is not available inside Metro Trains. however toilet facilities are available at metro stations in paid/unpaid area on Pay & Use basis.'

    if (('medical' in x or 'doctor' in x or 'first aid' in x) and ('available' in x or 'present' in x)):
        resp+='First Aid facility is available at all stations. For any medical emergency, ambulance service is also arranged through CAT.'


    #Luggage

    if ('allowed weight' in x or 'maximumm weight' in x or 'luggage limit' in x):
        resp+='''In DMRC:- One bag containing personal belongings not exceeding 80 cm x 50 cm x 30 cm in size
and 25 Kgs in gross weight is permitted. Baggage in form of bundles arenot permitted.
In Airport Express Line:- Two bags containing personal belongings not exceeding 90 cm x 75 cm x 45 cm in
size and 32 Kgs in gross weight is permitted. Baggage in form of bundles are not permitted.'''


    #Feeder Bus

    if ('feeder bus' in x and ('all' in x or 'every' in x)):
        resp+='No it is available at selected stations.'

    if ('feeder bus' in x and 'free' in x and 'pay' in x and 'metro' in x):
        resp+='No,you have to pay for the feeder bus services. '

    if ('card' in x and 'feeder' in x):
        resp+='Only AC feeder buses accepts smart card as mode of payment.'


    #Miscellaneous

    if ('emergency' in x or 'alarm' in x):
        resp+='It is a communication system provided in train for Communication between passenger and Train Operator in case of someemergencies.'

    #if ('interchange' in x or 'switch' in x):
     #   resp+='theta'

    if ('train timing' in x or 'timing' in x):
        resp+='The last train timings towards all terminals are displayed on every Customer Care Centre of all Metro stations or you may contact 24x7 DMRC Helpline number. Kindly get assistance from on duty staff before making entry in paid area.'

    if ('operating hours' in x or 'working hours' in x or 'hours' in x):
        resp+='Metro services are generally available from 06:00 AM to 11:00 PM'

    if ('frequency' in x or 'number' in x):
        resp+='In Delhi metro time interval between two consecutive trains varies from 2 minutes 30 seconds to 5 minutes on different lines while On Airport line it is 10 minutes.'

    if ('train closing' in x):
        resp+='Train stops on platform for the given dwell times & before the train doors start closing a warning sound is always played which lasts for about 2 to4 seconds. For your own safety, when you hear the sound for door closing you are required to stand off the train immediately. You should never try to enter in train while doors are closing as you may get hurt and it will unnecessarily delay the train. Moreover, obstructing door-closingis a punishable offence.'

    if ("late" in x):
        resp+="No,such facilities are not being by provided by the metro authorities. "

    if ('drinking water' in x):
        resp+='Drinking water facility @Rs. 2 per glass is available through kiosks at almost all the metro stations and where the said facility is not available then the commuters can ask for drinking water from the staff members available at such metro station.'

    if (('rapid metro' in x or ('gurugram' in x and 'metro' in x)) and 'interchange' in x):
        resp+='Sikanderpur Metro station on Yellow Line.'

    if ('baby stroller' in x):
        resp+='When entering the premises customers should hold up their children and fold strollers.'

    if ('queue for ladies' in x or 'quueue for senior citizens' in x):
        resp+='Only for ladies separate queue is available for security check. Except this no separate queues are available for ladies/Sr. citizens at any other location.'

    if ('exact change counter' in x):
        resp+='At exact change counter, a passenger having exact amount to purchase token can buy the tokens.'

    if ('route map' in x):
        resp+='Route maps are pasted at Customer Care Centres at all stations. You can also download the same from DMRC website.'

    if ('temperature setting' in x or 'air conditioning' in x):
        resp+='It is decided on the basis of ambient temperature and adequate level of comfort to the passengers.'

    if ('ladies ooaches' in x):
        resp+='Yes, DMRC has introduced one separate ladies coach in each train to ensure safe rides for women. Male Children up to the age of 12 years are only allowed to travel in ladies coach if accompanied by a women passenger.'

    if ('metro museum' in x):
        resp+='At Patel Chowk Metro Station on Yellow line.'

    if ('photographs permitted' in x or 'photographs' in x):
        resp+='No,photographs are no permitted here. '

    if ('eat ' in x or 'drink' in x):
        resp+='No,please dont eat or drink in the metro premises. '

    if (('sqaut on floor' in x or 'sit on floor' in x) and 'can' in x):
        resp+='No,please dont squat on the floor. '

    if ('play music' in x and 'can' in x):
        resp+='No,please dont play music and try to avoid inconvenience to fellow commuters. '

    if ('hang bag' in x):
        resp+='No, please don’t hang your bag on back to avoid inconvenience to fellow commuters and travel light.'

    if ('run on stairs' in x or 'run on escalators' in x):
        resp+='Please keep to the left while walking in subway stations, on stairs and escalators.'

    if ('disruption' in x or 'mid section stoppage' in x or 'stoppage' in x):
        resp+='Please follow the instructions of DMRC staff.'

    if ('parking' in x):
        resp+='Parking contractor manages the parking at metro station. Name & contact details are displayed at the board near parking entrance'

    if ('cleanliness' in x):
        resp+='Concerned civic agencies and municipal corporations are responsible for cleanliness outside metro station.'

    if ('traffic problem' in x):
        resp+='Traffic Police is responsible for traffic around metro station. Further, passenger may contact Traffic Police at Helpline number.'

    #Extra

    if ('fare' in x):
        resp+='Metro Fares depend upon distance of journey ranging from Rupees 10 to Rupees 60 with 10 as step'

    if 'dmrc' in x:
        resp+='DMRC is DELHI METRO RAIL CORPORATION official governing body of Delhi Metro in Delhi NCR'

    if 'dmtc' in x:
        resp+='DELHI METRO TRANSIT CORPORATION (unofficial)'

    return resp
