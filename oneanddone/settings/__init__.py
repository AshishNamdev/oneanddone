from .base import *

if 'DYNO' in os.environ:
    from .heroku import *
else:
    try:
        from .local import *
    except ImportError, exc:
        exc.args = tuple(['%s (did you rename settings/local.py-dist?)' % exc.args[0]])
        raise exc
