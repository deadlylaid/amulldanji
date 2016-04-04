import os
from .base import PROJECT_ROOT_DIR, BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# collectstatic할때 파일이 생성되는 경로
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')


STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'applications': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/application.css',
        },
    },
    'JAVASCRIPT': {
        'stats': {
            'source_filenames': (
                'js/jquery.js',
                'js/d3.js',
                'js/collections/*.js',
                'js/application.js',
            ),
            'output_filename': 'js/stlye.js',
        }
    }
}


PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
