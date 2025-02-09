'''
RunPod Tips
'''

import sys
import runpod.serverless.modules.logging as log


def check_return_size(return_body):
    '''
    Checks the size of the return body.
    If the size is above 2MB, it will recommend using storage upload.
    '''
    size = sys.getsizeof(return_body)
    size_mb = round(size / 1000000, 2)

    if size_mb > 2:
        log.tip(f"""Your return body is {size_mb} MB which exceeds the 2 MB limit.
                    Consider using S3 upload, returning the objects URL instead.""")
