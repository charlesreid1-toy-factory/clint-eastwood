import os
import sys
import logging
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed


logger = logging.getLogger(__name__)


def polite_print(quiet, msg):
    if not quiet:
        print(msg)


def run_cmd(self, cmd, cwd=os.getcwd(), shell=True):
    """Run a command and return stdout"""
    p = subprocess.Popen(cmd,
                         shell=shell,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         cwd=cwd,
                         env=self.stage_env)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        raise RuntimeError(f'While running a command, an error occured:\n'
                           f'stdout: {stdout}\n\n'
                           f'stderr: {stderr}\n')
    return stdout.decode('utf-8')


def map_results(func, blob_store):
    """
    Call `func` on an iterable of keys
    func is expected to be thread safe.
    """
    with ThreadPoolExecutor(max_workers=parallelization) as e:
        futures = list()
        for pfx in "0123456789abcdef":
            f = e.submit(func, blob_store.list(prefix=pfx))
            futures.append(f)
        for f in as_completed(futures):
            try:
                yield f.result()
            except Exception:
                logger.error(traceback.format_exc())
