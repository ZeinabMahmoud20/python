
class Person: 
    moods=('happy','tired','lazy')
    def __init__(self,name,money,mood,health_rate):
        self.name=name
        self.money=money
        self.mood=mood
        self.health_rate=health_rate
   
    def sleep(self,hours):
        if hours==7:
            print ("Happy")
        elif hours<7:
            print("Tired")
        else:
            print("Lazy")
    def eat(self,meal):
        if meal==3:
            print ("100 % Healthy")
        elif meal==2:
            print("75% healthy")
        else:
            print("50 % Healthy")
    def buy(self,item):
        if item==1:
            self.money-=10
            print(self.money)

class Employee(Person):
    def __init__(self, id, car,email,salary,distanceToWork,name,money,mood,health_rate):
        super(Employee,self).__init__(name,money,mood,health_rate)
        # self.Car=car
        if salary>1000:
            self.salary=salary
        else:
            salary=1000
        if health_rate >0 and health_rate<100:
            self.health_rate=health_rate
        else:
            health_rate=0
        self.car=car
    def work(self,hours):
        if hours==8:
            print ("Happy")
        elif hours>8:
            print("Tired")
        else:
            print("Lazy")
    def refuel(self,gasAmount=100):
        
        gasAmount+=c1.fuelRate
        print(gasAmount)
    def send_email(self,subject, from_email,to_email,sender_name):
        self.subject=subject
        self.from_email=from_email
        self.to_email=to_email
        self.sender_name=sender_name
        f1= open('save_email.txt','w')
        f1.write('subject is '+subject+'\n sender is '+from_email+'\n reciever is '+to_email+'\n'+sender_name)
    def drive(self):
        print("run with distance"+str(self.car.velocity))
        
    def distanceToWork(self,distance):
        print("distance is"+distance)

class Office:
    def __init__(self, name, Employee):
        self.name=name
        self.Employee=Employee
    def get_all_employees(self):
        pass
    def get_employee(self):
        pass
    def hire(self):
        pass
    def calculate_lateness(self):
        pass
    def deduct(self):
        pass
    def reward(self):
        pass

class Car:
    def __init__(self,name, fuelRate, velocity):
        self.name=name
        self.fuelRate=fuelRate
        self.velocity=velocity


        if velocity>0 and velocity<200:
            self.velocity=velocity
        else:
            velocity=0
        if fuelRate >0 and fuelRate< 100:
            self.fuelRate=fuelRate
        else:
            fuelRate=0
    
    def run(self,distance):
        self.fuelRate-=1
        # self.velocity=velocity
        time=distance/self.velocity
        # Car.stop()
        # print("run with distance "+ str(distance)+" and volcity is "+str(self.velocity)+ "in time ="+str(time))

    def stop(self):
        self.velocity=0
 
p1=Person("Samy",3300,'sleepy','aa@email.com')
p1.sleep(10)
p1.eat(2)
p1.buy(1)
c1=Car('BMW',120,30)
c1.run(10)
# (self, id, car,email,salary,distanceToWork,name,mood,health_rate)
e1= Employee(1,c1,'zeineb@email.com',10000,'120 KM','Salma',10000000000,'lazy',70)
e1.drive()
e1.refuel()
sub= input('Enter the subject')
from_email= input('Enter the sender email')
to_email= input('Enter the reciever email')
sender_name= input('Enter your name')
e1.send_email(sub, from_email,to_email,sender_name)
