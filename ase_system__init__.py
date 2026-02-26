"""
Autonomous Strategic Evolution (ASE) Trading System
Core package for autonomous trading strategy research and development
"""

__version__ = "1.0.0"
__author__ = "ASE Ecosystem"

from .config import ASEConfig
from .data_collector import DataCollector
from .strategy_researcher import StrategyResearcher
from .backtester import Backtester
from .risk_manager import RiskManager

__all__ = [
    "ASEConfig",
    "DataCollector",
    "StrategyResearcher",
    "Backtester",
    "RiskManager"
]