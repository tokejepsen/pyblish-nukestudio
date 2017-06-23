import hiero

import pyblish.api


class CollectSubmission(pyblish.api.ContextPlugin):
    """Collect submisson children."""

    order = pyblish.api.CollectorOrder - 0.1

    def process(self, context):

        context.data["submission"] = hiero.submission
