import os
from .base import PROJECT_ROOT_DIR, BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# collectstatic할때 파일이 생성되는 경로
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# 파이프라인에서 scss 와 js 파일을 잡고
# 각각 application.css / style.js 로 컴파일 합니다.
PIPELINE = {
    'STYLESHEETS': {
        'amulldanji': {
            'source_filenames': (
              'css/application.css',
            ),
            'output_filename': 'css/amulldanji.css',
        },
        'vendor': {
            'source_filenames': (
              'css/vendor/bootstrap.min.css',
              'css/vendor/mdb.css',
              'css/vendor/style.css',
            ),
            'output_filename': 'css/vendor/vendor.css',
        },
    },
    'JAVASCRIPT': {
        'amulldanji': {
            'source_filenames': (
                'js/application.js',
            ),
            'output_filename': 'js/amulldanji.js',
            },
        'vendor': {
            'source_filenames': (
              'js/vendor/jquery.min.js',
              'js/vendor/bootstrap.min.js',
              'js/vendor/mdb.js',
              'js/vendor/salvattore.min.js',
            ),
            'output_filename': 'js/vendor/vendor.js',
        },
    }
}

# yuglify -> CSS, JS 파일을 압축해줍니다.
PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
# PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
