from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSiteMap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated_date

