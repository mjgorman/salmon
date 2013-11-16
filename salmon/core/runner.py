import base64
import os
from logan.runner import run_app
from salmon.settings import base as base_settings

KEY_LENGTH = 40


def generate_settings():
    """
    This command is run when ``default_path`` doesn't exist, or ``init`` is
    run and returns a string representing the default data to put into their
    settings file.
    """
    conf_file = os.path.join(os.path.dirname(base_settings.__file__),
                             'example', 'conf.py')
    conf_template = open(conf_file).read()
    default_url = 'http://salmon.example.com'
    site_url = raw_input("What will be the URL for Salmon? [{0}]".format(
        default_url))
    site_url = site_url or default_url
    secret_key = base64.b64encode(os.urandom(KEY_LENGTH))
    api_key = base64.b64encode(os.urandom(KEY_LENGTH))
    output = conf_template.format(api_key=api_key, secret_key=secret_key,
                                  site_url=site_url)
    return output


def main():
    run_app(
        project='salmon',
        default_config_path='~/.salmon/conf.py',
        default_settings='salmon.settings.base',
        settings_initializer=generate_settings,
        settings_envvar='SALMON_CONF',
    )

if __name__ == '__main__':
    main()
