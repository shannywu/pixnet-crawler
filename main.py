# -*- coding: utf-8 -*-

import codecs
import json
import get_article as ga
import get_user_id as guid


def get_bloggers(category, page, period):
    return guid.get_user_ids(category, page, period)


def write_to_file_by_user(user_id, total_articles, user_rank, articles):
    """Save user's infomation and articles to a file in json format

    user_id - (str)
    total_articles - number of articles written by the user (int)
    user_rank - user rank in the category (int)
    articles - articles written by the user (list)
    """
    res = {
        "user_id": user_id,
        "total_articles": total_articles,
        "user_rank": user_rank,
        "articles": articles
    }
    with codecs.open('articles/' + user_id + '.json', 'w', encoding='utf8') as fout:
        json.dump(res, fout, ensure_ascii=False, indent=4)


def main():
    user_ids = get_bloggers(16, 1, '2018-05-01')

    for rank, user_id in enumerate(user_ids):
        print(user_id)
        article_meta = ga.get_hot_article_meta(user_id, 'total')
        try:
            articles = article_meta['articles']
        except:
            print(article_meta)
            continue

        articles_simple = []
        for article in articles:
            if article['site_category'] == '國外旅遊':
                articles_simple.append(ga.get_article_content(article['id'], user_id))
        if len(articles_simple) > 0:
            write_to_file_by_user(user_id, article_meta['total'], rank + 1, articles_simple)


if __name__ == '__main__':
    main()
