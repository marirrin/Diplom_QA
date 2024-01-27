# Кряженкова Марина, 12 когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


def test_get_order_by_track():
    response_order = sender_stand_request.create_order(data.body_create_order)
    track = {"t": response_order.json()["track"]}

    response_order_by_track = sender_stand_request.get_order_by_track(track)

    assert response_order_by_track.status_code == 200
