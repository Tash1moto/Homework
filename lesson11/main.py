# from psycopg2 import connect
#
# with connect(dsn="postgres://user1:8nycw4nyc9g4wy49@217.76.60.77:6666/user1") as conn:
#     with conn.cursor() as cur:
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS TAGS(
        #     id serial primary key,
        #     name varchar(16) not null unique check (length(name) >=2 )
        #     );
        # """)
        # cur.execute("""
        #     create table if not exists topics(
        #     id serial primary key,
        #     title varchar(128) not null check (length(title) >=2 ),
        #     body text not null,
        #     date_created timestamp not null default (now()),
        #     is_published boolean not null default (false)
        #     );
        # """)
        # cur.execute("""
        #     create table if not exists topic_tags(
        #     tag_id integer,
        #     topic_id integer,
        #     primary key (tag_id, topic_id),
        #     foreign key (tag_id) references tags(id) on delete restrict on update cascade,
        #     foreign key (topic_id) references topics(id) on delete restrict on update cascade
        #     );
        #     """)
        # conn.commit()

from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, TIMESTAMP, ForeignKey, CheckConstraint, TEXT)
from sqlalchemy.orm import DeclarativeBase, declarative_base
class Base(DeclarativeBase):
    ...

class Tag(Base):
    __tablename__ = "tags"
    id = Column(INT, primary_key=True)
    name