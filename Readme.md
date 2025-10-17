# 🏦 MacroMind

A real-time macroeconomic analytics platform with AI-powered insights and alerts.

## 🎯 Overview

MacroMind is a FastAPI-based application that provides real-time economic data analysis and AI-generated insights. The platform fetches economic indicators from the Federal Reserve, analyzes market conditions, and delivers intelligent alerts to help users understand macroeconomic trends.

## ✨ Features

* **📊 Real-time Economic Data** : Automatic fetching and updating of key economic indicators from FRED API
* **🤖 AI-Powered Insights** : Intelligent analysis of economic conditions using advanced algorithms
* **🚨 Alert System** : Automated alerts for significant economic events and trends
* **🔌 RESTful API** : Clean, well-documented API endpoints for easy integration
* **💚 Health Monitoring** : Built-in health checks and system status monitoring
* **📈 Trading Signals** : Basic trading recommendations based on economic conditions

## 📁 Project Structure

```
macromind/
├── macromind-backend/          # Backend API server
│   ├── api/                    # API endpoints
│   │   ├── __init__.py
│   │   ├── health.py          # Health check endpoints
│   │   ├── indicators.py      # Economic indicators API
│   │   └── insights.py        # AI insights and alerts API
│   ├── app/                    # Core application logic
│   │   ├── __init__.py
│   │   ├── agent.py           # Economic Intelligence Agent
│   │   ├── config.py          # Configuration settings
│   │   ├── data_fetcher.py    # FRED API data fetching
│   │   ├── models.py          # Pydantic data models
│   │   └── utils.py           # Helper functions
│   ├── tests/                  # Test suite
│   │   ├── __init__.py
│   │   ├── test_api.py
│   │   └── test_agent.py
│   ├── .env.example           # Environment variables template
│   ├── .gitignore            # Git ignore rules
│   ├── main.py               # Application entry point
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # This file
└── macromind-frontend/        # Frontend application (planned)
```

## 🔌 API Endpoints

### 📊 Economic Indicators

* `GET /api/indicators` - Get all economic indicators
* `GET /api/indicators/{indicator_name}` - Get specific indicator (GDP, UNEMPLOYMENT, INFLATION, FED_FUNDS, CONSUMER_SENTIMENT)

### 🤖 AI Insights

* `GET /api/insights` - Get AI-generated economic insights and analysis
* `GET /api/alerts` - Get current economic alerts and warnings

### 💚 Health

* `GET /api/health` - System health check and status
* `GET /` - API information and available endpoints

## 🚀 Quick Start

### Prerequisites

* Python 3.8+
* pip or conda
* FRED API key (free from [St. Louis Fed](https://fred.stlouisfed.org/docs/api/api_key.html))

### Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd macromind/macromind-backend
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure environment:**

```bash
cp .env.example .env
# Edit .env and add your FRED API key
```

4. **Run the application:**

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### 🔑 Getting FRED API Key

1. Visit [FRED API Key Registration](https://fred.stlouisfed.org/docs/api/api_key.html)
2. Sign up for a free account
3. Request an API key
4. Add it to your `.env` file:

```bash
FRED_API_KEY=your_actual_api_key_here
```

### 📚 API Documentation

Once the server is running, you can access:

* **Interactive API docs** : `http://localhost:8000/docs`
* **ReDoc documentation** : `http://localhost:8000/redoc`
* **API endpoints** : `http://localhost:8000/api/`

## 💡 Usage Examples

### Get All Economic Indicators

```bash
curl http://localhost:8000/api/indicators
```

### Get AI Economic Insights

```bash
curl http://localhost:8000/api/insights
```

### Get Current Alerts

```bash
curl http://localhost:8000/api/alerts
```

### Check System Health

```bash
curl http://localhost:8000/api/health
```

## 🛠️ Development

### Running Tests

```bash
cd macromind-backend
pytest tests/
```

### Environment Configuration

Create a `.env` file with the following variables:

```bash
# Required
FRED_API_KEY=your_fred_api_key_here

# Optional
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=true
LOG_LEVEL=INFO
```

### Code Structure

* **`main.py`** : FastAPI application entry point
* **`app/config.py`** : Configuration and settings management
* **`app/models.py`** : Pydantic data models for API responses
* **`app/agent.py`** : Economic Intelligence Agent with analysis logic
* **`app/data_fetcher.py`** : FRED API integration and data fetching
* **`api/`** : API endpoint definitions organized by functionality

## 🧠 Economic Intelligence Agent

The AI agent provides:

* **Economic Health Assessment** : Scores overall economic conditions (strong/moderate/weak)
* **Multi-factor Analysis** : Evaluates employment, inflation, growth, sentiment, and monetary policy
* **Automated Insights** : Generates natural language summaries of economic conditions
* **Risk Detection** : Identifies economic concerns and opportunities
* **Alert Generation** : Creates warnings for significant economic changes
* **Trading Signals** : Basic recommendations for bonds, equities, and USD

## 📊 Supported Economic Indicators

| Indicator          | FRED Series ID | Description                               |
| ------------------ | -------------- | ----------------------------------------- |
| GDP                | GDP            | Gross Domestic Product                    |
| UNEMPLOYMENT       | UNRATE         | Unemployment Rate                         |
| INFLATION          | CPIAUCSL       | Consumer Price Index                      |
| FED_FUNDS          | FEDFUNDS       | Federal Funds Rate                        |
| CONSUMER_SENTIMENT | UMCSENT        | University of Michigan Consumer Sentiment |

## 🔮 Technology Stack

* **Backend** : FastAPI, Python 3.8+
* **Data Processing** : Pandas, NumPy
* **HTTP Client** : HTTPX for async API calls
* **Data Models** : Pydantic for validation
* **Server** : Uvicorn ASGI server
* **Testing** : Pytest
* **Environment** : python-dotenv

## 🚧 Features in Development

* [ ] Frontend web application (React.js)
* [ ] Enhanced AI models with ML forecasting
* [ ] Additional economic indicators (10Y Treasury, VIX, etc.)
* [ ] Real-time WebSocket notifications
* [ ] Historical data analysis and backtesting
* [ ] Custom alert configuration
* [ ] Data visualization charts
* [ ] Multi-country economic analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure tests pass (`pytest tests/`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://claude.ai/chat/LICENSE) file for details.

## 🙏 Acknowledgments

* [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/) for providing free economic data APIs
* [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
* [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation

## 📧 Contact

* **Author** : Chanakya Vasantha
* **Email** : [your-email@example.com]
* **LinkedIn** : [your-linkedin-profile]
* **GitHub** : [your-github-username]

---

**⭐ Star this repository if you found it helpful!**
