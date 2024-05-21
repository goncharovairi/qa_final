# Гончарова Ирина, 1-я когорта — Финальный проект. Инженер по тестированию плюс

#!/usr/bin/python3
import sender_stand_request
import data


def test_order_creation_and_get_by_track_number():
    """Создание заказа и проверка получения данных по трек номеру"""
    # Создание заказа
    request_body = data.order_template_json.copy()
    response = sender_stand_request.create_order(request_body)
    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

    # Получние заказа по трек номеру и проверка статуса ответа
    order_response = sender_stand_request.get_order_by_track(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
