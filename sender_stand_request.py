import requests

import data

import configuration


def post_new_order(create_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=create_order,
                         headers=data.headers)


response = post_new_order(data.order_body)

track_order = response.json()["track"]


def get_order_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER,
                        params={"t": track_order})
