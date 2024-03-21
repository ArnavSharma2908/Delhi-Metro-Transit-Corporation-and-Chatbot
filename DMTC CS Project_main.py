import time
t1=time.time()#

print(' __          __  _                              _            _____    __  __   _______    _____ ')
print(' \ \        / / | |                            | |          |  __ \  |  \/  | |__   __|  / ____|')
print('  \ \  /\  / /__| | ___ ___  _ __ ___   ___    | |_ ___     | |  | | | \  / |    | |    | |     ')
print('   \ \/  \/ / _ \ |/ __/ _ \|  _ ` _ \ / _ \   | __/ _ \    | |  | | | |\/| |    | |    | |     ')
print('    \  /\  /  __/ | (_| (_) | | | | | |  __/   | || (_) |   | |__| | | |  | |    | |    | |____ ')
print('     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    \__\___/    |_____/  |_|  |_|    |_|     \_____|')

print('Starting GUI Screen...')

try:
    from Modules import *
except ModuleNotFoundError:
    raise Exception("Support File(s) of DMTC main python program not found probably due to changes performed in investigatory project folder\nTry running the DMTC main python file with required Investigatory project folder as its directory\nor\nPlease dowload the original soure code and project folder from this link: 'https://1drv.ms/u/s!Agq2cPQ6k4hagZcECq0rbiBejgCUjg?e=64tNoB'")

list_dir=os.listdir()
req_dir=[]
for i in req_dir:
    if i not in list_dir:
        raise Exception("Support File(s) of DMTC main python program not found probably due to changes performed in investigatory project folder\nTry running the DMTC main python file with required Investigatory project folder as its directory\nor\nPlease dowload the original soure code and project folder from this link: 'https://1drv.ms/u/s!Agq2cPQ6k4hagZcECq0rbiBejgCUjg?e=64tNoB'")


from GUI import *


x_co_extracter = lambda co: co[0]
y_co_extracter = lambda co: co[1]
def plot_map():
    figure(figsize=(7, 5), dpi=100)
    for i in csvlist:
        lisx=[]
        lisy=[]
        if i[0] in ('Line Info',''):
            continue
        if i[0][0]!='C':
            plt.plot(list(map(x_co_extracter,list(map(get_coordinates,i[1:i.index('')])))),\
                     list(map(y_co_extracter,list(map(get_coordinates,i[1:i.index('')])))),\
                     marker='.',ms=2,mfc='black',mec='black',c=i[0][3:i[0].index('L')-1])

def get_line(st):
    linenames_set=set()
    for line in csvlist:
        if st in line:
            linenames_set.add(line[0])
    return linenames_set

def get_route(st1,st2):
    setA=get_line(st1)
    if st1==st2 and len(setA)!=0:
        return [st1],setA.pop()
    setB=get_line(st2)
    common_line_name=setA.intersection(setB)
    routes=[]
    linenames_func=[]
    try:
        while True:
            linename=common_line_name.pop()
            lineinfo1=(csvlist[eval(linename[0:2])*2])
            lineinfo2=list(reversed(lineinfo1))
            routes.append(lineinfo1[lineinfo1.index(st1):lineinfo1.index(st2)+1]+lineinfo2[lineinfo2.index(st1):lineinfo2.index(st2)+1])
            linenames_func.append(linename)
    except:
        return short_route_generat(routes,linenames_func)

def short_route_generat(routes,linenames):
    index=list(map(get_avg_distance,routes)).index(min(list(map(get_avg_distance,routes))))
    return routes[index],linenames[index]

get_coordinates=lambda st: eval(csvlist[eval(get_line(st).pop()[0:2])*2+1][csvlist[eval(get_line(st).pop()[0:2])*2].index(st)])[::-1]
def get_avg_distance(route):
    avg_distance=0
    for i in route[1:]:
        avg_distance+=pow((get_coordinates(i)[0]-get_coordinates(route[route.index(i)-1])[0])**2+(get_coordinates(i)[1]-get_coordinates(route[route.index(i)-1])[1])**2,1/2)
    return avg_distance

def log_dump(dump_data):
    if log_dump_loc=='MySQL RDBMS':
        cur.execute('insert into dmtc_logs values'+str(dump_data))
    elif log_dump_loc=='Binary File':
        pickle.dump(dump_data,logs)
    else:
        raise ValueError()

print('DELHI METRO TRANSIT CORPORATION PROGRAM')
print('This will lead you through journey of Delhi and NCR from one place to another via DMTC Stations and its planning')

try:
    password=input('Enter MySQL Client password:')
    con=sqlcon.connect(host='localhost',user='root',password=password)
    '''
    if con.is_connected():
        print("MySQL-Python Connection Established")
    else:
        raise Exception('Connection Failed')
    '''
    cur=con.cursor()
    log_dump_loc='MySQL RDBMS'

    try:
        cur.execute('create database dmtc_database;')
        print('No Existing Database for DMTC operations Creating New Database for operations')
    except:
        print('DataBase exists for DMTC operations')
    cur.execute('use dmtc_database;')
    
    try:
        cur.execute('create table dmtc_logs (date_inputed datetime,Initial_Station varchar(25),\
Destined_Station varchar(25),Execution_Load_Duration_in_seconds decimal,Result varchar(10));')
        print('No Existing Table detected for DMTC logs maintanance Creating New Table for Storage of logs')
    except:
        print('Table exists for logs dumping and maintanance')
    
    try:
        with open('bin_dmtc_templogs.dat','rb') as logs:
            while True:
                values=pickle.load(logs)
                cur.execute('insert into dmtc_logs values'+str(values))
    except EOFError:
        print('bin_dmtc_templogs.dat file data is successfully extracted and dumped into mysql database\
,file has been removed')
        os.remove('bin_dmtc_templogs.dat')
        con.commit()
    except FileNotFoundError:
        print('No log_temp File Detected')
        
except:
    print('Unable to estabilish connection between MySQL and Python probably due to Incorrect Password')
    print('  therefore carrying forward the log data dumping to binary file bin_log_dump.dat')
    logs=open('bin_dmtc_templogs.dat','ab')
    log_dump_loc='Binary File'

f=open('DMTC Stations CS Database.csv')
csvlist=list(csv.reader(f))
plot_map()
t2=time.time()#
init_st,dest_st=gui_input_station()
init_st=init_st.upper()
dest_st=dest_st.upper()
t3=time.time()#

if len(get_line(init_st).intersection(get_line(dest_st)))in (1,2):
    route,linename=get_route(init_st,dest_st)
    linename=linename[3:]

elif len(get_line(init_st).intersection(get_line(dest_st)))==0:
    routes=[]
    linenames=[]
    for i1 in get_line(init_st):
        for i2 in csvlist[int(i1[0:2])*2]:
            if i2=='':
                break
            if len(get_line(i2).intersection(get_line(dest_st)))!=0:
                phase1,linename1=get_route(init_st,i2)
                phase2,linename2=get_route(i2,dest_st)
                routes.append(phase1+phase2)
                linenames.append(linename1[3:]+' and '+linename2[3:])
                route,linename=short_route_generat(routes,linenames)
                
    if not routes:
        for i1 in get_line(init_st):
            for i2 in get_line(dest_st):
                for i3 in csvlist[int(i1[0:2])*2]:
                    if i3=='':
                        break
                    for i4 in csvlist[int(i2[0:2])*2]:
                        if i4=='':
                            break
                        if len(get_line(i3).intersection(get_line(i4)))!=0:
                            phase1,linename1=get_route(init_st,i3)
                            phase2,linename2=get_route(i3,i4)
                            phase3,linename3=get_route(i4,dest_st)
                            routes.append(phase1+phase2+phase3)
                            linenames.append(linename1[3:]+', '+linename2[3:]+' and '+linename3[3:])
                            route,linename=short_route_generat(routes,linenames)
try:
    prevst=route[0]
    plt.annotate(init_st,(get_coordinates(init_st)[0]+0.005,get_coordinates(init_st)[1]+0.005),size=5)
    plt.annotate(dest_st,(get_coordinates(dest_st)[0]+0.005,get_coordinates(dest_st)[1]+0.005),size=5)
    avg_distance=get_avg_distance(route)*100
    if avg_distance==0:
        fare=0
    elif avg_distance>0 and avg_distance<=2:
        fare=10
    elif avg_distance>2 and avg_distance<=5:
        fare=20
    elif avg_distance>5 and avg_distance<=12:
        fare=30
    elif avg_distance>12 and avg_distance<=21:
        fare=40
    elif avg_distance>21 and avg_distance<=32:
        fare=50
    elif avg_distance>32:
        fare=60
    if (datetime.date.today().isoweekday==7 or int(str(datetime.date.today().day)\
                                                   +str(datetime.date.today().month))in (261,158,210)) and fare>=20:
        fare-=10
    print('Your route is as follows via',linename,'('+str(t2-t1+time.time()-t3)+') seconds')#,end='')
    gui_print_station('Board')
    dump_data=(str(datetime.datetime.now()),init_st,dest_st,t2-t1+time.time()-t3,'Success')
    log_dump(dump_data)
    for stprnt in route:
        if prevst==stprnt!=route[0]:
            gui_print_station('Change here')#,end='')
            plt.scatter(get_coordinates(stprnt)[0],get_coordinates(stprnt)[1],c='yellow',s=50)
            plt.annotate(stprnt,get_coordinates(stprnt),size=5)
        else:
            plt.arrow(get_coordinates(prevst)[0],get_coordinates(prevst)[1],get_coordinates(stprnt)[0]-get_coordinates(prevst)[0],get_coordinates(stprnt)[1]-get_coordinates(prevst)[1],head_width=0.01,ec='lime',alpha=.5,width=0.01)
        gui_print_station('→',stprnt)#,end='')
        prevst=stprnt
        time.sleep(0.1)
    gui_print_station('Deboard')
    print('Average_distance=',avg_distance,'Km','and Fare=',fare)
    plt.scatter(get_coordinates(init_st)[0],get_coordinates(init_st)[1],c='green',s=50)
    plt.scatter(get_coordinates(dest_st)[0],get_coordinates(dest_st)[1],c='red',s=50)
    
except:
    print('Incorrect Station names, Try again by referring to map shown at beginning')
    dump_data=(str(datetime.datetime.now()),init_st,dest_st,t2-t1+time.time()-t3,'Error')
    log_dump(dump_data)
plt.title('Delhi Transit route map',size=15,c='black')
plt.xlabel('x coordinates (1 unit = 100Km)')
plt.ylabel('y coordinates (1 unit = 100Km)')

if log_dump_loc=='MySQL RDBMS':
    con.commit()
    con.close()
elif log_dump_loc=='Binary File':
    logs.close()
else:
    raise ValueError()

final_display()
plt.show()
while True:
    close()
    display()
