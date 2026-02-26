"""
Real-time and historical market data collector
Handles data fetching, cleaning, and storage in Firebase
"""
import asyncio
import ccxt
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
import logging
from datetime import datetime, timedelta
from .config import ASEConfig, ExchangeType, TimeFrame
import