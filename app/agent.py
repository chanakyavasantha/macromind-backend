# app/agent.py - Economic Intelligence Agent

import numpy as np
from datetime import datetime
from typing import Dict, List, Optional

from .models import EconomicIndicator, AgentInsight, AlertMessage

class EconomicIntelligenceAgent:
    def __init__(self):
        self.last_analysis = None
        self.alerts = []
    
    def analyze_economic_conditions(self, indicators: Dict[str, EconomicIndicator]) -> AgentInsight:
        """Analyze current economic conditions and generate insights"""
        
        # Score different aspects of the economy
        employment_score = self._score_employment(indicators.get("UNEMPLOYMENT"))
        inflation_score = self._score_inflation(indicators.get("INFLATION"))
        growth_score = self._score_growth(indicators.get("GDP"))
        sentiment_score = self._score_sentiment(indicators.get("CONSUMER_SENTIMENT"))
        monetary_score = self._score_monetary_policy(indicators.get("FED_FUNDS"))
        
        # Calculate overall economic health (handle None values)
        scores = [score for score in [employment_score, inflation_score, growth_score, sentiment_score, monetary_score] if score is not None]
        overall_score = np.mean(scores) if scores else 5.0
        
        # Determine economic health category
        if overall_score >= 7:
            health = "strong"
        elif overall_score >= 5:
            health = "moderate"
        else:
            health = "weak"
        
        # Generate key concerns and opportunities
        concerns = self._identify_concerns(indicators)
        opportunities = self._identify_opportunities(indicators)
        
        # Generate summary
        summary = self._generate_summary(health, indicators, concerns, opportunities)
        
        return AgentInsight(
            timestamp=datetime.now().isoformat(),
            economic_health=health,
            key_concerns=concerns,
            opportunities=opportunities,
            confidence=min(overall_score / 10, 1.0),
            summary=summary
        )
    
    def _score_employment(self, unemployment: Optional[EconomicIndicator]) -> Optional[float]:
        """Score employment conditions (0-10)"""
        if not unemployment:
            return None
        
        rate = unemployment.latest_value
        if rate <= 3.5:
            return 10.0
        elif rate <= 4.5:
            return 8.0
        elif rate <= 6.0:
            return 6.0
        elif rate <= 8.0:
            return 4.0
        else:
            return 2.0
    
    def _score_inflation(self, cpi: Optional[EconomicIndicator]) -> Optional[float]:
        """Score inflation conditions (0-10)"""
        if not cpi:
            return None
        
        # Calculate inflation volatility (simplified)
        change = abs(cpi.change_percent)
        if change <= 2.5:  # Near Fed target
            return 9.0
        elif change <= 4.0:
            return 7.0
        elif change <= 6.0:
            return 5.0
        else:
            return 3.0
    
    def _score_growth(self, gdp: Optional[EconomicIndicator]) -> Optional[float]:
        """Score economic growth (0-10)"""
        if not gdp:
            return None
        
        change = gdp.change_percent
        if change >= 3.0:
            return 9.0
        elif change >= 2.0:
            return 7.0
        elif change >= 1.0:
            return 6.0
        elif change >= 0:
            return 4.0
        else:
            return 2.0
    
    def _score_sentiment(self, sentiment: Optional[EconomicIndicator]) -> Optional[float]:
        """Score consumer sentiment (0-10)"""
        if not sentiment:
            return None
        
        value = sentiment.latest_value
        if value >= 100:
            return 9.0
        elif value >= 90:
            return 7.0
        elif value >= 80:
            return 6.0
        elif value >= 70:
            return 4.0
        else:
            return 3.0
    
    def _score_monetary_policy(self, fed_funds: Optional[EconomicIndicator]) -> Optional[float]:
        """Score monetary policy stance (0-10)"""
        if not fed_funds:
            return None
        
        rate = fed_funds.latest_value
        trend = fed_funds.trend
        
        # Contextual scoring based on current economic environment
        if rate <= 2.0 and trend == "stable":
            return 8.0  # Accommodative
        elif rate <= 5.0 and trend == "up":
            return 6.0  # Tightening but reasonable
        elif rate > 5.0:
            return 4.0  # Restrictive
        else:
            return 7.0
    
    def _identify_concerns(self, indicators: Dict[str, EconomicIndicator]) -> List[str]:
        """Identify key economic concerns"""
        concerns = []
        
        if "UNEMPLOYMENT" in indicators:
            unemployment = indicators["UNEMPLOYMENT"]
            if unemployment.latest_value > 6.0:
                concerns.append(f"High unemployment at {unemployment.latest_value}%")
            elif unemployment.trend == "up":
                concerns.append("Rising unemployment trend")
        
        if "INFLATION" in indicators:
            inflation = indicators["INFLATION"]
            if abs(inflation.change_percent) > 5.0:
                concerns.append(f"High inflation volatility: {inflation.change_percent}%")
        
        if "GDP" in indicators:
            gdp = indicators["GDP"]
            if gdp.change_percent < 0:
                concerns.append("Negative GDP growth")
        
        if "CONSUMER_SENTIMENT" in indicators:
            sentiment = indicators["CONSUMER_SENTIMENT"]
            if sentiment.latest_value < 70:
                concerns.append("Low consumer confidence")
        
        if "FED_FUNDS" in indicators:
            fed_funds = indicators["FED_FUNDS"]
            if fed_funds.latest_value > 6.0:
                concerns.append("High interest rates constraining growth")
        
        return concerns
    
    def _identify_opportunities(self, indicators: Dict[str, EconomicIndicator]) -> List[str]:
        """Identify economic opportunities"""
        opportunities = []
        
        if "UNEMPLOYMENT" in indicators:
            unemployment = indicators["UNEMPLOYMENT"]
            if unemployment.latest_value < 4.0:
                opportunities.append("Strong labor market supports consumer spending")
            elif unemployment.trend == "down":
                opportunities.append("Improving employment conditions")
        
        if "FED_FUNDS" in indicators:
            fed_funds = indicators["FED_FUNDS"]
            if fed_funds.trend == "down":
                opportunities.append("Easing monetary policy supports growth")
            elif fed_funds.latest_value < 3.0:
                opportunities.append("Low interest rates support investment")
        
        if "CONSUMER_SENTIMENT" in indicators:
            sentiment = indicators["CONSUMER_SENTIMENT"]
            if sentiment.trend == "up":
                opportunities.append("Improving consumer confidence")
            elif sentiment.latest_value > 90:
                opportunities.append("High consumer confidence drives spending")
        
        if "GDP" in indicators:
            gdp = indicators["GDP"]
            if gdp.change_percent > 2.5:
                opportunities.append("Strong economic growth momentum")
        
        if "INFLATION" in indicators:
            inflation = indicators["INFLATION"]
            if abs(inflation.change_percent) < 2.0:
                opportunities.append("Stable inflation supports economic planning")
        
        return opportunities
    
    def _generate_summary(self, health: str, indicators: Dict, concerns: List[str], opportunities: List[str]) -> str:
        """Generate economic summary"""
        summary_parts = [f"Economic health is currently {health}."]
        
        if concerns:
            summary_parts.append(f"Key concerns include: {', '.join(concerns[:2])}.")
        
        if opportunities:
            summary_parts.append(f"Opportunities: {', '.join(opportunities[:2])}.")
        
        # Add specific indicator context
        context_parts = []
        if "UNEMPLOYMENT" in indicators:
            unemp = indicators["UNEMPLOYMENT"].latest_value
            context_parts.append(f"unemployment at {unemp}%")
        
        if "INFLATION" in indicators:
            infl = indicators["INFLATION"].change_percent
            context_parts.append(f"inflation trend at {infl}%")
        
        if "FED_FUNDS" in indicators:
            fed_rate = indicators["FED_FUNDS"].latest_value
            context_parts.append(f"fed funds rate at {fed_rate}%")
        
        if context_parts:
            summary_parts.append(f"Current conditions: {', '.join(context_parts)}.")
        
        return " ".join(summary_parts)
    
    def check_alerts(self, indicators: Dict[str, EconomicIndicator]) -> List[AlertMessage]:
        """Check for alert conditions"""
        alerts = []
        current_time = datetime.now().isoformat()
        
        for key, indicator in indicators.items():
            # High change alerts
            if abs(indicator.change_percent) > 10:
                severity = "critical" if abs(indicator.change_percent) > 20 else "warning"
                alerts.append(AlertMessage(
                    severity=severity,
                    indicator=indicator.name,
                    message=f"{indicator.name} changed by {indicator.change_percent}%",
                    timestamp=current_time
                ))
            
            # Specific threshold alerts
            if key == "UNEMPLOYMENT" and indicator.latest_value > 7.0:
                alerts.append(AlertMessage(
                    severity="critical",
                    indicator=indicator.name,
                    message=f"Unemployment rate high at {indicator.latest_value}%",
                    timestamp=current_time
                ))
            
            if key == "INFLATION" and abs(indicator.change_percent) > 6.0:
                alerts.append(AlertMessage(
                    severity="warning",
                    indicator=indicator.name,
                    message=f"High inflation volatility: {indicator.change_percent}%",
                    timestamp=current_time
                ))
            
            if key == "FED_FUNDS" and indicator.latest_value > 6.0:
                alerts.append(AlertMessage(
                    severity="warning",
                    indicator=indicator.name,
                    message=f"Federal funds rate elevated at {indicator.latest_value}%",
                    timestamp=current_time
                ))
            
            if key == "CONSUMER_SENTIMENT" and indicator.latest_value < 60:
                alerts.append(AlertMessage(
                    severity="warning",
                    indicator=indicator.name,
                    message=f"Consumer sentiment low at {indicator.latest_value}",
                    timestamp=current_time
                ))
        
        return alerts
    
    def get_trading_signals(self, indicators: Dict[str, EconomicIndicator]) -> Dict[str, str]:
        """Generate basic trading signals based on economic conditions"""
        signals = {}
        
        # Bond signals based on Fed policy
        if "FED_FUNDS" in indicators:
            fed_funds = indicators["FED_FUNDS"]
            if fed_funds.trend == "up":
                signals["bonds"] = "SELL - Rising rates hurt bond prices"
            elif fed_funds.trend == "down":
                signals["bonds"] = "BUY - Falling rates support bond prices"
            else:
                signals["bonds"] = "HOLD - Stable rates"
        
        # Equity signals based on growth and employment
        if "GDP" in indicators and "UNEMPLOYMENT" in indicators:
            gdp = indicators["GDP"]
            unemployment = indicators["UNEMPLOYMENT"]
            
            if gdp.change_percent > 2.0 and unemployment.latest_value < 5.0:
                signals["equities"] = "BUY - Strong growth and employment"
            elif gdp.change_percent < 0 or unemployment.latest_value > 7.0:
                signals["equities"] = "SELL - Weak economic conditions"
            else:
                signals["equities"] = "HOLD - Mixed signals"
        
        # Dollar signals based on rates and growth
        if "FED_FUNDS" in indicators and "GDP" in indicators:
            fed_funds = indicators["FED_FUNDS"]
            gdp = indicators["GDP"]
            
            if fed_funds.trend == "up" and gdp.change_percent > 1.5:
                signals["dollar"] = "BUY - Rising rates and growth support USD"
            elif fed_funds.trend == "down" and gdp.change_percent < 1.0:
                signals["dollar"] = "SELL - Falling rates and weak growth"
            else:
                signals["dollar"] = "HOLD - Neutral conditions"
        
        return signals

# Initialize global agent
intelligence_agent = EconomicIntelligenceAgent()