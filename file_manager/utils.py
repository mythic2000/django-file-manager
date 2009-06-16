import urllib
import os

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def get_max_upload_size():
    if not settings.FILE_UPLOAD_MAX_SIZE:
        raise ImproperlyConfigured, 'file_manager requires FILE_UPLOAD_MAX_SIZE variable be defined in settings.py' 

    return settings.FILE_UPLOAD_MAX_SIZE

def get_document_root():
    if not settings.DOCUMENT_ROOT:
        raise ImproperlyConfigured, 'file_manager requires DOCUMENT_ROOT variable be defined in settings.py' 

    return settings.DOCUMENT_ROOT

def clean_path(url):
    """
    Makes the path safe from ..
    """
    if not url:
        return '' 

    result = ''
    path = os.path.normpath(urllib.unquote(url))
    path = path.lstrip('/')
    for part in path.split('/'):
        if not part:
            # Strip empty path components.
            continue
        drive, part = os.path.splitdrive(part)
        head, part = os.path.split(part)
        if part in (os.curdir, os.pardir):
            # Strip '.' and '..' in path.
            continue
        result = os.path.join(result, part).replace('\\', '/')
        
    if result and path != result or not path:
        result = ''
    
    return result
