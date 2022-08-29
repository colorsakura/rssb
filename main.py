# coding: utf-8

from requests import get
import json
import rtoml
import aiohttp


def parse_option():
    with open("./config.toml") as f:
        config = rtoml.load(f)
    return config


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
    items = parse_option()["anime"]
    for item in items:
        write_rss_xml(item["name"], get_rss(item["url"]))


if __name__ == '__main__':
    run()
