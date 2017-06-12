import psycopg2

DBNAME = 'news'


def top_articles():
    """Returns the three most popular articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select articles.title, count(log.path) as num
            from articles left join log
                on log.path like concat('%', articles.slug)
            group by articles.title
            order by num desc limit 3;
        """)
    posts = c.fetchall()
    db.close()
    return posts


def top_authors():
    """Returns sum of articles author has written in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
    select authors.name, sum(article_count.num)
        from (select articles.author, count(log.path) as num
            from articles left join log
                on log.path like concat('%', articles.slug)
            group by articles.author
            order by num desc)
        as article_count
        join authors
            on article_count.author = authors.id
        group by authors.name
        order by sum desc;
        """)

    posts = c.fetchall()
    db.close()
    return posts


def request_errors():
    """Returns days where more than 1% of requests leads to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select *
            from (select
                date(time),
                round((sum(case when status != '200 OK' then 1 else 0 end)
                * 100.0 / count(status)), 2)
            as percent
            from log
            group by cast(log.time as date))
            as daily_errors
            where percent > 1.0;
        """)
    posts = c.fetchall()
    db.close()
    return posts


def make_txt_file():
    """Turns queries into text file"""
    file = open("sql_query_results.txt","w+")
    for line in top_articles():
        print line
        file.write(line[0] + ' ' + str(line[1]))
        file.write('\n')
    file.write('\n')
    for line in top_authors():
        print line
        file.write(line[0] + ' ' + str(line[1]))
        file.write('\n')
    file.write('\n')
    for line in request_errors():
        print line
        file.write(str(line[0]) + ' ' + str(line[1]))
        file.write('\n')
    file.close()


if __name__ == '__main__':
    make_txt_file()
