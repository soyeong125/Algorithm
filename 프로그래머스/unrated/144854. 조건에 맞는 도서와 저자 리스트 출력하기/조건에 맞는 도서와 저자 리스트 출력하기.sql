select a.BOOK_ID,
       b.AUTHOR_NAME,
       date_format(a.PUBLISHED_DATE,'%Y-%m-%d') PUBLISHED_DATE
from book a, author b
where a.author_id = b.author_id
  and a.category = '경제'
order by PUBLISHED_DATE