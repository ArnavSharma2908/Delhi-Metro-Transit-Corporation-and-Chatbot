from Modules import sg
from Modules import os

sg.theme('DarkAmber')

layout=[]
route_Listbox=[]
layout2=["[sg.Image(filename='Img2.png')]","[sg.Button('Call Metrobot')]","[sg.Button('See Documentations')]"]
font=("Segoe Print", 10)
list_of_stations = ['ADARSH NAGAR', 'AIIMS', 'AIRPORT (T-3)', 'AKSHARDHAM', 'ANAND VIHAR ISBT', 'ARJAN GARH', 'ARTHALA', 'ASHOK PARK MAIN', 'ASHRAM',\
                    'AZADPUR', 'BADARPUR BORDER', 'BADKAL MOR', 'BAHADURGARH CITY', 'BARAKHAMBA ROAD', 'BATA CHOWK', 'BHIKAJI CAMA PLACE',\
                    'BOTANICAL GARDEN', 'BRIG. HOSHIAR SINGH', 'CENTRAL SECRETARIAT', 'CHANDNI CHOWK', 'CHAWRI BAZAR', 'CHHATARPUR', 'CHIRAG DELHI',\
                    'CIVIL LINES', 'DABRI MOR - JANAKPURI SOUTH', 'DASHRATHPURI', 'DELHI AEROCITY', 'DELHI CANTT.', 'DELHI GATE', 'DHANSA BUS STAND',\
                    'DHAULA KUAN', 'DILLI HAAT - INA', 'DILSHAD GARDEN', 'DURGABAI DESHMUKH SOUTH CAMPUS', 'DWARKA', 'DWARKA MOR', 'DWARKA SECTOR - 10',\
                    'DWARKA SECTOR - 11', 'DWARKA SECTOR - 12', 'DWARKA SECTOR - 13', 'DWARKA SECTOR - 14', 'DWARKA SECTOR - 2', 'DWARKA SECTOR - 21',\
                    'DWARKA SECTOR - 8', 'DWARKA SECTOR - 9', 'EAST AZAD NAGAR', 'EAST VINOD NAGAR-MAYUR VIHAR', 'ESCORTS MUJESAR', 'ESI-BASAIDARAPUR',\
                    'GHEVRA METRO STATION', 'GHITORNI', 'GOKULPURI', 'GOLF COURSE', 'GOVINDPURI', 'GREATER KAILASH', 'GREEN PARK', 'GURU DRONACHARYA',\
                    'GURU TEG BAHADUR NAGAR', 'HAIDERPUR BADLI MOR', 'HARKESH NAGAR OKHLA', 'HAUZ KHAS', 'HINDON RIVER', 'HUDA CITY CENTRE',\
                    'I.P. EXTENSION', 'IFFCO CHOWK', 'IIT', 'INDERLOK', 'INDRAPRASTHA', 'ITO', 'JAFRABAD', 'JAHANGIRPURI', 'JAMA MASJID',\
                    'JAMIA MILIA ISLAMIYA', 'JANAK PURI EAST', 'JANAK PURI WEST', 'JANGPURA', 'JANPATH', 'JASOLA VIHAR SHAHEEN BAGH', 'JASOLA-APOLLO',\
                    'JHANDEWALAN', 'JHILMIL', 'JLN STADIUM', 'JOHRI ENCLAVE', 'JOR BAGH', 'KAILASH COLONY', 'KALINDI KUNJ', 'KALKAJI MANDIR',\
                    'KANHAIYA NAGAR', 'KARKARDUMA', 'KARKARDUMA COURT', 'KAROL BAGH', 'KASHMERE GATE', 'KAUSHAMBI', 'KESHAV PURAM', 'KHAN MARKET',\
                    'KIRTI NAGAR', 'KOHAT ENCLAVE', 'KRISHNA NAGAR', 'LAJPAT NAGAR', 'LAL QUILA', 'LAXMI NAGAR', 'LOK KALYAN MARG', 'MADIPUR',\
                    'MAHARAJA SURAJMAL STADIUM', 'MAJLIS PARK', 'MAJOR MOHIT SHARMA RAJENDRA NAGAR', 'MALVIYA NAGAR', 'MANDAWALI - WEST VINOD NAGAR',\
                    'MANDI HOUSE', 'MANSAROVAR PARK', 'MAUJPUR-BABARPUR', 'MAYAPURI', 'MAYUR VIHAR - 1', 'MAYUR VIHAR EXTENSION', 'MAYUR VIHAR POCKET-1',\
                    'MEWALA MAHARAJPUR', 'MG ROAD', 'MODEL TOWN', 'MOHAN ESTATE', 'MOHAN NAGAR', 'MOOLCHAND', 'MOTI NAGAR', 'MUNDKA',\
                    'MUNDKA INDUSTRIAL AREA (MIA)', 'MUNIRKA', 'NAJAFGARH', 'NANGLI', 'NANGLOI', 'NANGLOI RAILWAY STATION', 'NARAINA VIHAR', 'NAWADA',\
                    'NEELAM CHOWK AJRONDA', 'NEHRU ENCLAVE', 'NEHRU PLACE', 'NETAJI SUBHASH PLACE', 'NEW ASHOK NAGAR', 'NEW DELHI', 'NHPC CHOWK',\
                    'NIRMAN VIHAR', 'NOIDA CITY CENTRE', 'NOIDA ELECTRONIC CITY', 'NOIDA SECTOR-15', 'NOIDA SECTOR-16', 'NOIDA SECTOR-18', \
                    'OKHLA BIRD SANCTUARY', 'OKHLA NSIC', 'OKHLA VIHAR', 'OLD FARIDABAD', 'PALAM', 'PANCHSHEEL PARK', 'PANDIT SHREE RAM SHARMA',\
                    'PASCHIM VIHAR EAST', 'PASCHIM VIHAR WEST', 'PATEL CHOWK', 'PATEL NAGAR', 'PEERAGARHI', 'PITAMPURA', 'PRATAP NAGAR', 'PREET VIHAR',\
                    'PULBANGASH', 'PUNJABI BAGH', 'PUNJABI BAGH WEST', 'QUTAB MINAR', 'R.K.PURAM', 'RAJ BAGH', 'RAJA NAHAR SINGH(BALLABHGARH)',\
                    'RAJDHANI PARK', 'RAJENDRA PLACE', 'RAJIV CHOWK', 'RAJOURI GARDEN', 'RAMAKRISHNA ASHRAM MARG', 'RAMESH NAGAR', 'RITHALA',\
                    'ROHINI EAST', 'ROHINI SECTOR - 18, 19', 'ROHINI WEST', 'SADAR BAZAR CANTONMENT', 'SAKET', 'SAMAYPUR BADLI', 'SANT SURDAS (SIHI)',\
                    'SARAI', 'SARAI KALE KHAN - NIZAMUDDIN', 'SARITA VIHAR', 'SAROJINI NAGAR', 'SATGURU RAM SINGH MARG', 'SECTOR - 52 NOIDA',\
                    'SECTOR-28', 'SECTOR-34 NOIDA', 'SECTOR-59 NOIDA', 'SECTOR-61 NOIDA', 'SECTOR-62 NOIDA', 'SEELAMPUR', 'SHADIPUR', 'SHAHDARA',\
                    'SHAHEED NAGAR', 'SHAHEED STHAL (NEW BUS ADDA)', 'SHAKURPUR', 'SHALIMAR BAGH', 'SHANKAR VIHAR', 'SHASTRI NAGAR', 'SHASTRI PARK',\
                    'SHIV VIHAR', 'SHIVAJI PARK', 'SHIVAJI STADIUM', 'SHYAM PARK', 'SIKANDERPUR', 'SIR M. VISHWESHWARAIAH MOTI BAGH',\
                    'SOUTH EXTENSION', 'SUBHASH NAGAR', 'SUKHDEV VIHAR', 'SULTANPUR', 'SUPREME COURT', 'TAGORE GARDEN', 'TERMINAL 1-IGI AIRPORT',\
                    'TIKRI BORDER', 'TIKRI KALAN', 'TILAK NAGAR', 'TIS HAZARI', 'TRILOKPURI-SANJAY LAKE', 'TUGHLAKABAD STATION', 'UDYOG BHAWAN',\
                    'UDYOG NAGAR', 'UTTAM NAGAR EAST', 'UTTAM NAGAR WEST', 'VAISHALI', 'VASANT VIHAR', 'VIDHAN SABHA', 'VINOBAPURI',\
                    'VISWAVIDYALAYA', 'WELCOME', 'YAMUNA BANK']


def print(*x):
    newx=''
    tempx=''
    for i in x:
        newx+=str(i)+' '
    global layout
    for i in newx:
        if i=='\n':
            layout.append("[sg.Text(tempx)]".replace('tempx','\''+tempx+'\''))
            tempx=''
        else:
            tempx+=i
    layout.append("[sg.Text(tempx)]".replace('tempx','\''+tempx+'\''))

def gui_print_station(*x):
    newx=''
    global route_Listbox
    for i in x:
        newx+=str(i)+' '
    route_Listbox.append(newx)
    if newx=='Deboard ':
        layout.append("[sg.Listbox("+str(route_Listbox)+",size=(20,10))]")

def input(x):
    layout.append("[sg.Text(x),sg.InputText(),sg.Button('Ok')]".replace('(x)','(\''+x+'\')'))
    tabgrp=[[sg.TabGroup([[sg.Tab('Main Tab',list(map(eval,layout))),sg.Tab('Options',list(map(eval,layout2)))]]),sg.Column([[sg.Image('Img.png')],[sg.Button('Close')]])]]
    window=sg.Window('Window title',tabgrp,font=font,resizable=True).Finalize()
    #window.Maximize()
    
    event='init'
    while event in ('Call Metrobot','See Documentations','init'):
        event,gui_values=window.read()
        if event=='Call Metrobot':
            os.startfile('Metrobot.py')
        elif event=='See Documentations':
            os.startfile('CS Investigatory project report.pdf')

    if event in ('Close',None) or gui_values is None:
        window.close()
        os._exit(True)
    layout[-1]=("[sg.Text(x),sg.StatusBar('"+list(gui_values.values())[0]+"',size=(4,1))]").replace('(x)','(\''+x+'\')')
    window.close()
    return gui_values[0]

def gui_input_station():
    layout.append("[sg.Text('Enter Initial Station Name:'),sg.Combo(list_of_stations,size=(20,10))]")
    layout.append("[sg.Text('Enter Destined Station Name:'),sg.Combo(list_of_stations,size=(20,10))]")
    layout.append("[sg.Button('Get Route')]")
    tabgrp=[[sg.TabGroup([[sg.Tab('Main Tab',list(map(eval,layout))),sg.Tab('Options',list(map(eval,layout2)))]]),sg.Column([[sg.Image('Img.png')],[sg.Button('Close')]])]]
    window=sg.Window('Window title',tabgrp,font=font,resizable=True).Finalize()
    
    event='init'
    while event in ('Call Metrobot','See Documentations','init'):
        event,gui_values=window.read()
        if event=='Call Metrobot':
            os.startfile('Metrobot.py')
        elif event=='See Documentations':
            os.startfile('CS Investigatory project report.pdf')

    if event in ('Close',None):# or gui_values[0] == '' or gui_values[1] == '':
        os._exit(True)
    window.close()
    layout[-3]=("[sg.Text('Enter Initial Station Name:'),sg.StatusBar('"+gui_values[0]+"')]")
    layout[-2]=("[sg.Text('Enter Destined Station Name:'),sg.StatusBar('"+gui_values[1]+"')]")
    layout[-1]=("[sg.Text('')]")
    return gui_values[0],gui_values[1]

def display():
    global window
    tabgrp=[[sg.TabGroup([[sg.Tab('Main Tab',list(map(eval,layout))),sg.Tab('Options',list(map(eval,layout2)))]]),sg.Column([[sg.Image('Img.png')],[sg.Button('Close')]])]]
    window=sg.Window('Window title',tabgrp,font=font,resizable=True).Finalize()
    
    read_data=('init',None)
    while read_data[0] in ('Call Metrobot','See Documentations','init'):
        read_data=window.read()
        if read_data[0]=='Call Metrobot':
            os.startfile('Metrobot.py')
        elif read_data[0]=='See Documentations':
            os.startfile('CS Investigatory project report.pdf')

    if read_data[0]=='Close' or read_data[0]==sg.WIN_CLOSED:
        os._exit(True)
    return read_data

def close():
    window.close()

def final_display():
    layout.append("[sg.Button('Show Route Map')]")
    event,values=display()

