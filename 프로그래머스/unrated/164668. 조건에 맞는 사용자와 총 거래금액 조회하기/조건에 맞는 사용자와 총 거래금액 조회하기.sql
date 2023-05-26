

select b.user_id, b.nickname,sum(a.price) total_sales
from USED_GOODS_BOARD a, USED_GOODS_USER b
where a.writer_id = b.user_id
  and a.STATUS = 'DONE' 
group by b.user_id
having total_sales >= 700000
order by total_sales

