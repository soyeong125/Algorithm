select month(START_DATE) MONTH, car_id, count(*) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in
(select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
group by car_id
having count(car_id) >= 5
) and date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
group by car_id , month(START_DATE)
having RECORDS > 0
order by MONTH, car_id desc