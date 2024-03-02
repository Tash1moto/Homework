from psycopg2 import connect
conn = connect("postgres://user1:8nycw4nyc9g4wy49@217.76.60.77:6666/user1")
cur = conn.cursor()

cur.execute("""
    select * from chats inner join (
    select chat_id from chats_relations inner join users on
    (chats_relations.department = users.department AND chats_relations.sub_department = users.sub_department))
    on id.chats = chat_id.chats_relations
    """)
print(cur.fetchall())
