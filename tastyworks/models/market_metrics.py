import logging
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List

import requests
from dataclasses import dataclass, field

from tastyworks.models.security import Security

LOGGER = logging.getLogger(__name__)


class Market_Metrics:
    @staticmethod
    def get_market_metrics(session, symbols: List[str] ,**kwargs) -> any : 
        """
        Gets all market metrics.

        Args:
            session (TastyAPISession): The session to use.
            symbold : list of symbols to get data from
        Returns:
            List/Dict: market metrics
        """
        if not session.logged_in:
            raise Exception('Tastyworks session not logged in.')

        url = f"{session.API_url}/market-metrics?{','.join(symbols)}"

        res = requests.get(url,headers=session.get_request_headers())
        return res
        



