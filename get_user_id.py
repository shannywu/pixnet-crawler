# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

PIXNET_BLOG_RANKING_PAGE = 'https://pixranking.events.pixnet.net/ranking/'


def get_user_ids(category, page, period):
    """Get user ID of top ranked blogs.

    ategory - category ID (int)
    page - given page, 100 blogs per page (int)
    period - ranking period, Y-m-d (str)

    return user_id (str)
    """
    result = requests.post(PIXNET_BLOG_RANKING_PAGE, data={
        'category': category,
        'page': page,
        'period': period
    })

    soup = BeautifulSoup(result.text, 'html.parser')
    blog_user_name = soup.find_all(id='blogUserName')
    blog_links = [name['href'] for name in blog_user_name if 'blog' in name['href']]

    user_id = []
    for link in blog_links:
        user_id.append(re.sub(r'http://|/blog|\.pixnet\.net|www\.|\.tw|\.com|', '', link))

    return user_id
