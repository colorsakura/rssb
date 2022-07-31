# coding: utf-8

from requests import get
import json


def get_data():
    with open("data.json", 'r') as f:
        rss_url = json.load(f)
    return rss_url


def get_rss(url):
    resp = get(url)
    return resp.content.decode('UTF-8')


def write_rss_xml(name, xml):
    with open("./rss/{}.xml".format(name), 'w+', encoding='UTF-8') as f:
        f.write(xml)


def run():
    rss_url = get_data()
    for name, value in rss_url.items():
        write_rss_xml(name, get_rss(value))


if __name__ == '__main__':
    run()
