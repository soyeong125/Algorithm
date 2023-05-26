select a.author_id, author_name, category,sum(sales*price) total_sales
from book a,author b, book_sales c
where a.book_id = c.book_id 
  and a.author_id = b.author_id
  and year(sales_date) = '2022' and month(sales_date) = 1
group by a.author_id, category
order by a.author_id, category desc