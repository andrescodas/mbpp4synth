def sorted_models(models):
 """
 Write a function to sort a list of dictionaries using lambda function.
 """
 sorted_models = sorted(models, key = lambda x: x['color'])
 return sorted_models
