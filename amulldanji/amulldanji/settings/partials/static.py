import os
from .base import PROJECT_ROOT_DIR, BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# collectstatic할때 파일이 생성되는 경로
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')

BASE_DIR2 = os.path.dirname(BASE_DIR)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR2, 'static'),
]

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
        'applications': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/application.css',
        },
        'vendor': {
            'source_filenames': (
              'css/vendor/*.css',
            ),
            'output_filename': 'css/vendor/vendor.css',
        },
    },
    'JAVASCRIPT': {
        'main_js': {
            'source_filenames': (
                'js/*.js',
            ),
            'output_filename': 'js/main.js',
            },
        'vendor': {
            'source_filenames': (
              'js/vendor/*.js',
            ),
            'output_filename': 'js/vendor/vendor.js',
        },
    }
}

# yuglify -> CSS, JS 파일을 압축해줍니다.
PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'

# sass -> SASS 파일을 CSS로 컴파일 해줍니다.
PIPELINE['COMPILERS'] = (
          'pipeline.compilers.sass.SASSCompiler',
          )
