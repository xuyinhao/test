import  pymysql

# 事务机制可以确保数据一致性。
# 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
# 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
# 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
global  cursor
global db
db = pymysql.connect("122.112.220.238",'root','passwd','wordpress')
cursor = db.cursor()
def select():
    sql="SELECT * FROM wp_users;"
    try:
        cursor.execute(sql)
        result= cursor.fetchall()
        for i in result:
            print(i)
        # print(result)
    except:
        print("error")

def insert_user():
    sql="insert into wp_users values (NULL,'Xyh','$P$BspNVYOrTjjbr4.0x6wkQxbXXTACO21','Xyh','xyh@xyh.com','','2019-11-12 10:00:10','',0,'Xyhxyh');"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("ex",e)
        db.rollback()


insert_user()
db.close()

