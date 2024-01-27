# Кряженкова Марина, 12 когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests


def create_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body_order)


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params=track)
