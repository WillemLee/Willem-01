#!/usr/bin/env python3
import sys,queue,configparser,getopt
from multiprocessing import Process
from datetime import datetime

queue1 = queue.Queue(0)
queue2 = queue.Queue(0)
global conf
opts, args = getopt.getopt(sys.argv[1:], 'C:c:d:o:h', ['help'])

#get config.cfg
class config():
    def __init__(self,confilename,cityname):
            self.cityname = cityname
            self.cityconf = {}
            self.cf = configparser.ConfigParser()
            self.cf.read(confilename)
            self.cityconf = self.cf.items(cityname)

    def get_config_num(self,cityname,name):
        return int(self.cf.getfloat(cityname,name))


class UserData():
    #get user.csv
    def __init__(self,userfile):
        self.userdata = {}
        with open(userfile,'r') as file:
            for x in file:
                x = x.split(',')
                a = x[0].strip(' ')
                b = x[1].strip(' ').strip('\n')
                self.userdata[a] = b
    #dictbecomelist
    def process_list(self):
        self.proc_list = []
        for key,value in self.userdata.items():
            self.proc_list.append(key+':'+value)
        return self.proc_list

    #calculator taxablecal
    def taxablecal(self,income):
        tax_inc = float(income) - float(self.insurance_cal(income)) - 3500
        if tax_inc <= 0:
            taxable = 0
        elif tax_inc <= 1500 and tax_inc > 0:
            taxable = tax_inc * 0.03
        elif tax_inc <= 4500 and tax_inc > 1500:
            taxable = tax_inc * 0.1 - 105
        elif tax_inc <= 9000 and tax_inc > 4500:
            taxable = tax_inc * 0.2 - 555
        elif tax_inc <= 35000 and tax_inc > 9000:
            taxable = tax_inc * 0.25 - 1005
        elif tax_inc <= 55000 and tax_inc > 35000:
            taxable = tax_inc * 0.3 - 2755
        elif tax_inc <= 80000 and tax_inc > 55000:
            taxable = tax_inc * 0.35 - 5505
        else:
            taxable = tax_inc * 0.45 - 13505
        return taxable

    def insurance_cal(self,income):
         all_ins=0
         for citynum in conf.cityconf:
             if int(float(citynum[1])) > 1:
                 continue
             else:
                 a=float(citynum[1])
                 all_ins+=a

         if income < conf.get_config_num(conf.cityname,'JiShuL'):
             insurance = conf.get_config_num(conf.cityname,'JiShuL') * all_ins
         elif income > conf.get_config_num(conf.cityname,'JiShuH') :
             insurance = conf.get_config_num(conf.cityname,'JiShuH') * all_ins
         else:
             insurance = income * all_ins
         return insurance

    def new_userlist(self,proc1_list):
        self.new_ul = []
        for x in proc1_list:
            x = x.split(':')
            a = x[0]
            b = x[1]
            c = format(self.insurance_cal(int(b)), '.2f')
            d = format(self.taxablecal(int(b)), '.2f')
            g = float(b) - self.insurance_cal(int(b)) - self.taxablecal(int(b))
            e = format(g, '.2f')
            h = datetime.now()
            f = datetime.strftime(h,'%Y-%m-%d %H:%M:%S')
            usrSalary = a+','+b+','+c+','+d+','+e+','+f
            self.new_ul.append(usrSalary)
        return list(self.new_ul)
    #?????????????????
    @staticmethod
    def dumptofile(userdata_csv,outputfile):
        #?????????
        with open(outputfile,'w') as file:
            #??????
                for x in userdata_csv:
                    user_detail = x.split(',')
                    file.write(','.join(i for i in user_detail))
                    file.write('\n')

#??1????????
def jincheng1(proc_list1):
    queue1.put_nowait(proc_list1)
#??2????????????
def jincheng2(u_file):
     data = queue1.get_nowait()
     a = UserData(u_file)
     new_data = a.new_userlist(data)
     queue2.put(list(new_data))
#??3???????????
def jincheng3(uindex,outputfile):
     data = queue2.get_nowait()
     UserData(uindex).dumptofile(data,outputfile)
#????
def main(p1arg,p2arg,p3arg):
    p1 = Process(target=jincheng1(p1arg))
    p2 = Process(target=jincheng2(p2arg))
    p3 = Process(target=jincheng3(p2arg,p3arg))
    p1.start()
    p2.start()
    p3.start()
#start
if __name__ == '__main__':
    cityname = 'DEFAULT'
    configindex = ''
    userindex = ''
    outputindex = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], 'C:c:d:o:h', ['help'])
    for opt_name, opt_value in opts:
        if opt_name not in ('-c','-d','-o','-C','-h','--help'):
            print('input error \n Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
        if opt_name in ('-h', '--help'):
            print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
        if opt_name in ('-c'):
            configindex = opt_value
        if opt_name in ('-d'):
            userindex = opt_value
            # do something
        if opt_name in ('-o'):
            outputindex = opt_value
        if opt_name in ('-C'):
            cityname = opt_value.upper()
    conf = config(configindex,cityname)
    userSalary = UserData(userindex)
    main(userSalary.process_list(), userindex, outputindex)
except getopt.GetoptError():
    print('Input error')
except:
    print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')

