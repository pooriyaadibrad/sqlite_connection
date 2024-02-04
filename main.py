from sqlalchemy import create_engine,Column,String,Integer

from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine("sqlite:///test.db",echo=True)

base=declarative_base()


sessions=sessionmaker(bind=engine)

session=sessions()

class human(base):
    __tablename__="humans"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    family=Column(String)
    age=Column(Integer)
    def __init__(self,name='',family='',age=0):
        self.name=name
        self.family=family
        self.age=age
base.metadata.create_all(engine)

human1=human(name="pooriya",family="adib",age=24)

session.add(human1)

session.commit()

alldata=session.query(human).all()

for data in alldata:
    print(data.name)


data1=session.query(human).filter(human.id==1).first()

print(data1.family)

data1=human(name="pooriya",family="pooriya",age=24)

session.commit()

data2=session.query(human).filter(human.id==1).first()

print(data2.family)
