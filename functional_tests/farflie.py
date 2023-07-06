from fabric.api import env, run


def _get_base_folder(host):
    return '~/sites/' + host


def _get_manage_dot_py(host):
    return f'{_get_base_folder(host)}/virtualenv/bin/python {_get_base_folder(host)}/source/manage.py'


def reset_database(host):
    run(f'{_get_manage_dot_py(env.host)} flush --noinput')


def create_session_on_server(email):
    session_key = run(f'{_get_manage_dot_py(env.host)} create_session {email}')
    print(session_key)