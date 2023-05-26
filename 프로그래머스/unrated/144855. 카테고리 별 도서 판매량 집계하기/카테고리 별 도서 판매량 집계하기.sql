-- 코드를 입력하세요
select a.category, sum(b.sales) total_sales
from book a, book_sales b
where a.book_id = b.book_id
 and date_format(b.sales_date,'%y-%m') = '22-01'
group by a.category
order by a.category