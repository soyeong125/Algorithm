select x.animal_id, x.name
from animal_outs x
where x.animal_id not in(
select o.animal_id
from animal_outs o, animal_ins i
where o.animal_id = i.animal_id
)
order by x.animal_id