# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

PIXNET_API_URI = 'https://emma.pixnet.cc/'


def get_article_meta(user_id, per_page, page):
    """Get article meta data

    user_id - (str)
    page - given page, default 1 (int)

    return article_meta_data
    """
    result = requests.get('{}blog/articles?user={}&format={}&per_page={}&page={}'.format(
        PIXNET_API_URI,
        user_id,
        'json',
        per_page,
        page
    ))
    article_meta_data = json.loads(result.text)

    return article_meta_data


def get_hot_article_meta(user_id, period):
    """Get popular articles of a user

    user_id - (str)
    period - daily, weekly, monthly, total(default) - (str)

    return hot_article_meta_data 
    """
    result = requests.get('{}blog/articles/hot?user={}&period={}&trim_user={}&format={}'.format(
        PIXNET_API_URI,
        user_id,
        period,
        1,
        'json'
    ))
    hot_article_meta_data = json.loads(result.text)

    return hot_article_meta_data


def parse_article_content(article_body):
    """Parse article body to get text content

    article_body - article in HTML format (str)

    return text of the body
    """
    soup = BeautifulSoup(article_body, 'html.parser')

    return soup.get_text()


def get_article_content(article_id, user_id):
    """Get content of an article

    article_id - (str)

    return content
    """
    result = requests.get('{}blog/articles/{}?user={}&format={}'.format(
        PIXNET_API_URI,
        article_id,
        user_id,
        'json'
    ))

    try:
        article_content = json.loads(result.text)['article']
        article_content_simple = {
            'id': article_content.get('id'),
            'title': article_content.get('title'),
            'public_at': article_content.get('public_at'),
            'category': article_content.get('site_category'),
            'link': article_content.get('link'),
            'hits': article_content.get('hits').get('total'),
            'tags': list(map(lambda x: x['tag'], article_content.get('tags'))),
            'content': parse_article_content(article_content.get('body'))
        }
        return article_content_simple
    except:
        pass
