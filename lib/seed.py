from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

# Create companies
company_1 = Company(name='Muranja', founding_year=2019)
company_2 = Company(name="Ztech", founding_year=2002)
company_3 = Company(name="Endarata", founding_year=2022)

# Create developers
developer_1 = Dev(name="Raph")
developer_2 = Dev(name="Edwin")
developer_3 = Dev(name="Wesley")

session.add_all([company_1, company_2, company_3, developer_1, developer_2, developer_3])
session.commit()

# Create freebies
freebie_1 = Freebie(item_name="Mechanical Keyboard", value=50000, dev= developer_1, company=company_2)
freebie_2= Freebie(item_name="Wireless mouse", value=70000, dev=developer_2, company=company_1)
freebie_3 = Freebie(item_name="USB-C Hub", value=5000, dev=developer_3, company=company_3)
freebie_4 = Freebie(item_name="Webcam", value=15000, dev=developer_1, company=company_3)
freebie_5 = Freebie(item_name="Earbuds", value=10000, dev=developer_2, company=company_1)

session.add_all([freebie_1, freebie_2, freebie_3, freebie_4,freebie_5])
session.commit()
