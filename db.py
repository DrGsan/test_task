import psycopg2 as pg


def create_db():
    """
    Создает таблицу, если ее еще нет в БД
    """
    with pg.connect('dbname=postgres user=postgres password=postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("""create table if not exists A (token_list varchar(255) not null)""")
            cur.execute("""create table if not exists B (token_list varchar(255) not null)""")
            cur.execute("""create table if not exists C (token_list varchar(255) not null)""")
            print('База данных и таблицы созданы')


def pg_db_connect(option, table, token_list=None):
    """
    :param table:
    :param option: Режим вызова функции.
        insert - вставка значений в БД
        check - проверка наличия значенияв БД
    :param token_list: Список  для проверки/вставки
    :return: возвращает список  из БД
    """
    with pg.connect('dbname=postgres user=postgres password=postgres') as conn:
        if option == 'insert':
            with conn.cursor() as cur:
                if table == 'A':
                    cur.execute("""insert into A (token_list) values (%s)""", (token_list,))
                elif table == 'B':
                    cur.execute("""insert into B (token_list) values (%s)""", (token_list,))
                elif table == 'C':
                    cur.execute("""insert into C (token_list) values (%s)""", (token_list,))
        elif option == 'check':
            with conn.cursor() as cur:
                if table == 'A':
                    cur.execute("""select token_list from A;""")
                elif table == 'B':
                    cur.execute("""select token_list from B;""")
                elif table == 'C':
                    cur.execute("""select token_list from C;""")
                result = cur.fetchall()
            return result


if __name__ == '__main__':
    pass
