from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))


def create_session_on_server(host, email):
    return subprocess.check_output([
        'fab',
        f'create_session_on_server:email={email}',
        f'--host={host}',
        f'--hide-everything,status',
    ],
        cwd=THIS_FOLDER
    ).decode.strip()


def reset_database(host):
    subprocess.check_call(
        ['fab',
         'reset_database',
         f'--host={host}'
         ],
        cwd=THIS_FOLDER
    )
