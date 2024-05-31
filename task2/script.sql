USE shurik

create TABLE wines (
    id int,
    country varchar(255),
    description text,
    designation text,
    points int,
    price int,
    province varchar(255),
    region_1 varchar(255),
    region_2 varchar(255),
    taster_name varchar(255),
    taster_twitter varchar(255),
    title varchar(255),
    variety varchar(255),
    winery varchar(255)
)
ENGINE = MergeTree()
order by id

--оставить только непустые значения для названий стран и цен
delete from wines
where price is null or price = 0
    or country is null or country = ''

--найти максимальную цену для каждой страны
select
    country
    , max(price)
from wines
group by country
order by max(price) desc

--вывести топ-10 стран с самыми дорогими винами (country, max_price)
select
    country
    , max(price)
from wines
group by country
order by max(price) desc
LIMIT 10

--определить как высокая цена коррелирует с оценкой дегустатора (насколько дорогие вина хорошие)
select
    corr(points, price) -- 0.42
from wines

--учесть в выборке также регион производства
select
    region_1,
    corr(points, price)
from wines
group by region_1
