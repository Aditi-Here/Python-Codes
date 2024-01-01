# # a = 45
# # b = 7
# # b=a+b  #12
# # a=b-a  #7
# # b=b-a #5
# #
# # print('a: ',a,'b= ',b )
# #----------------------------------------------------------------------------------
#

class Employee():
    def __init__(self,name,age,manager):
        self.age=age
        self.name=name
        self.manager=manager

obj1 = Employee('A',1,"Aditi")
obj2 = Employee('B',2,"Samarth")
obj3= Employee('C',3,"Aditi")

list = [obj1,obj2,obj3]
record={}
for k in list:
    if k.manager not in record.keys():
        record[k.manager]=[k.name]
        
    else:
         record[k.manager]+=k.name
# for key,value in record.items():
#     print("Person under manager",key,'is',value)

# --------------------------------------------------------------------------------

class Company():
    def __init__(self,id,name,manager):
        self.id=id
        self.name=name
        self.manager=manager

com1 = Company(1,'Patni','Aditi')
com2 = Company(2,'Math','Samarth')
com3 = Company(3,'Umlaut','Sowmya')

com_list=[com1,com2,com3]

# for i in com_list:
#   if i.manager not in record.keys():
#       print("The company is ", i.name, "and the persons under the manager  ", i.manager, "is empty")
#   else:
#     print("The company is ",i.name,"and the persons under the manager  ",i.manager,"is",record[i.manager])

record["Patni"]={'Sam':['A','B']}

company_dict={}
for i in com_list:
    company_dict[i.name]={i.manager:}

print("the dict of company ",company_dict)
