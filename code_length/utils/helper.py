import pymysql
from settings import Config


def connect():
    conn = Config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 取回的是字典
    return conn, cursor


def connect_close(conn, curser):
    conn.close()
    curser.close()


def fetch_one(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    connect_close(conn, cursor)
    return result


def fetch_all(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    result_list = cursor.fetchall()
    connect_close(conn, cursor)
    return result_list


def insert(sql, args):
    conn, cursor = connect()
    row = cursor.execute(sql, args)
    conn.commit()
    connect_close(conn, cursor)
    return row
