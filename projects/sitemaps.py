from django.contrib.sitemaps import Sitemap

from .models import RepositoryMetadata


class ProjectSiteMap(Sitemap):
    changefreq = "hourly"
    priority = 1

    def items(self):
        return RepositoryMetadata.objects.all()

    def lastmod(self, obj):
        return obj.last_updated
