from konectu.core.python_engine import PythonEngine
from konectu.core.context import Context, get_default_context
from konectu.core.extractors import (
    PythonFromMarkdownExtractor,
    JsonFromMarkdownExtractor,
)
from konectu.core.retrievers import OpsmSplitRetriever
from konectu.core.world_model import WorldModel
from konectu.core.utilities.version_checker import check_latest_version
from konectu.core.action_engine import ActionEngine
from konectu.core.agents import WebAgent

import os
import warnings


def telemetry_warning():
    telemetry_var = os.getenv("konectu_TELEMETRY")
    if telemetry_var != "NONE":
        warning_message = "\033[93mTelemetry is turned on. To turn off telemetry, set your konectu_TELEMETRY to 'NONE'\033[0m"
        warnings.warn(warning_message, UserWarning)


telemetry_warning()
try:
    check_latest_version()
except:
    pass
