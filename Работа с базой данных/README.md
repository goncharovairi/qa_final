#### Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

```sql
SELECT courier.login, COUNT(courier.id) AS "OrdersInDelivery"
FROM "Couriers" AS courier
LEFT JOIN "Orders" AS orders ON courier.id = orders."courierId"
WHERE orders."inDelivery" = true
GROUP BY courier.login;
```

#### Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
- Если поле finished == true, то вывести статус 2.
- Если поле canсelled == true, то вывести статус -1.
- Если поле inDelivery == true, то вывести статус 1.
 - Для остальных случаев вывести 0.

```sql
SELECT track,
       CASE
           WHEN finished = TRUE THEN 2
           WHEN cancelled = TRUE THEN -1
           WHEN "inDelivery" = TRUE THEN 1
           ELSE 0
       END AS status
FROM "Orders";
```

##### Предварительно необходимо создать курьера, создать и принять заказ etc. (в БД отсуствуют тестовые данные)
