from django.db import models

# Create your models here.
class Classifier(models.Model):
    app_label = 'classifier'

    name = models.CharField(max_length=100)
    random_forest_classifier = models.BooleanField(default=True)
    forest_tree_count = models.IntegerField(default=2000)
    confidence = models.IntegerField(default=0)
    svc_classifier = models.BooleanField(default=False)
    doc_stats = models.BooleanField(default=True)
    bow = models.BooleanField(default=True)
    tfidf_vectoriser = models.BooleanField(default=False)
    bow_vectoriser = models.BooleanField(default=True)
    vec_analyzer = models.CharField(max_length=20, default='word')
    vec_min_df = models.FloatField(default=0.001)
    vec_stop_words = models.CharField(max_length=20, default='english')
    vec_max_features = models.IntegerField(default=10000)
    vec_ngram_range_min = models.IntegerField(default=1)
    vec_ngram_range_max = models.IntegerField(default=3)
    vec_strip_accents = models.CharField(max_length=20, default='ascii')


    application = models.ForeignKey('application.Application')
    docset = models.ForeignKey('docset.DocSet')