import requests
import tenacity

from schemas.execute import BaseExecute


class Request:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, **kwargs) -> BaseExecute:

        @tenacity.retry(stop=tenacity.stop.stop_after_attempt(3), wait=tenacity.wait.wait_fixed(0.5))
        def _get():
            return self.session.get(url, **kwargs)

        base_execute = BaseExecute()
        try:
            response = _get()
        except tenacity.RetryError:
            base_execute.success, base_execute.message = False, "tenacity.RetryError"
        except Exception as e:
            base_execute.success, base_execute.message = False, str(e)
        else:
            base_execute.data = response.text
        return base_execute
