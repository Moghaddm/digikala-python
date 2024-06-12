
from django.utils.text import slugify
import random

def slugify_product_name(instance,save=False,new_slug=None):
    if new_slug is None:
        slug = slugify(instance.name)
    else:
        slug = new_slug
    Klass = instance.__class__
    qs = Klass.products.filter(slug =slug ).exclude(pk = instance.id)
    if qs.exists():
        rand = random.randint(300_000,500_000)
        slug = f"{slug}-{rand}"
        return slugify_product_name(instance,save=True,new_slug = slug)
    instance.slug= slug
    if save:
        instance.save()
    return instance
