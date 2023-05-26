-- 코드를 입력하세요
SELECT round(avg(daily_fee)) average_fee
from CAR_RENTAL_COMPANY_CAR
group by car_type
having car_type = 'suv'