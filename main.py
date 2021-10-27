from sqlalchemy import Table, create_engine, MetaData, inspect, Column, Integer, Float

engine = create_engine('sqlite:///cc3.db')

metadata = MetaData()
metadata.reflect(bind=engine)

cc_trans3Meta = MetaData()
cc_trans3 = Table(
    'cc_trans3', cc_trans3Meta,
    Column('ID', Integer, primary_key=True),
    Column('Time', Float),
    Column('V1', Float),
    Column('Amount', Float),
    Column('Class', Integer)
)

table_names = []
for table in metadata.tables.values():
    table_names.append(table.name)
    print(table.name)
    for column in table.c:
        print(column.name)

if not "cc_trans3" in table_names:
    cc_trans3Meta.create_all(engine)

cc_trans3 = metadata.tables['cc_trans3']
with engine.connect() as con:
    result = con.execute(cc_trans3.select())
    for row in result:
        print(row)

