#!/usr/bin/python3
import configuration
import requests
import data


def create_order(body):
    """Создание заказа"""
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_URI,
        headers=data.headers,
        json=body,
    )
    return response


def get_order_by_track(track_number):
    """Получение заказа по трек номеру"""
    response = requests.get(
        configuration.URL_SERVICE
        + configuration.TRACK_ORDER_URI
        + "?t="
        + str(track_number)
    )
    return response
