select a.car_id, a.car_type, round(a.daily_fee * (100-DISCOUNT_RATE)/100 * 30 ) fee
from CAR_RENTAL_COMPANY_CAR a, CAR_RENTAL_COMPANY_RENTAL_HISTORY b, CAR_RENTAL_COMPANY_DISCOUNT_PLAN c
where a.car_id = b.car_id
  and a.car_type = c.car_type
  and (a.car_type = '세단' or a.car_type = 'SUV')
  and a.car_id not in (
  select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where end_date > '2022-11-01' and start_date < '2022-12-01') 
  and c.DURATION_TYPE = '30일 이상'
group by a.car_id
having fee between 500000 and 2000000
order by fee desc ,car_type, car_id desc