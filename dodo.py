# Configuration for the "doit" tool.
DOIT_CONFIG = dict(
    # While running scripts, output everything the script is printing to the
    # screen.
    verbosity=2,

    # When the user executes "doit list", list the tasks in the order they are
    # defined in this file, instead of alphabetically.
    sort='definition',
)


def task_func():
    return dict(
        file_dep=['primes_func.py'],
        actions=['python primes_func.py']
    )


def task_script():
    return dict(
        file_dep=['primes_script.py'],
        actions=['python primes_script.py']
    )
