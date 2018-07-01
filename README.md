# PIXNET Crawler

Get articles on PIXNET through [PIXNET API](https://developer.pixnet.pro/#!/)

## Prerequisite

- Python 3.6
- requests
- BeautifulSoup

## Usage

- Get Top Ranked User ID
```python
import get_user_id as guid

user_ids = guid.get_user_ids(category, page, period)
```

- Get Hot Articles of an User
```python
import get_article as ga

article_meta = ga.get_hot_article_meta(user_id, 'total')
articles = article_meta['articles']
```

- Get Article Content
```python
import get_article as ga

article_content = get_article_content(article_id, user_id)
```