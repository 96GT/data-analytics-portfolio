import pandas as pd
import streamlit as st
import yfinance as yf


st.set_page_config(page_title="Stock Portfolio Analyzer", layout="wide")

st.title("Beginner Stock Portfolio Analyzer")
st.caption(
    "This app uses yfinance for learning purposes. Prices may be delayed and "
    "should not be treated as official real-time trading data."
)
st.info(
    "Shares and average purchase prices come from your brokerage position data. "
    "Current prices and daily changes are fetched from yfinance."
)


# Enter your real holdings here.
# Format: TICKER, SHARES OWNED, AVERAGE PURCHASE PRICE
DEFAULT_HOLDINGS = """Ticker,Shares,AveragePurchasePrice
HUT,0.526,75.89
IREN,2.331,42.79
NLR,0.073,136.71
NVDA,0.477,187.42
SCHG,2.84,31.67
URA,1.777,53.40"""


def parse_holdings(holdings_text):
    """Turn the user's typed holdings into a list of dictionaries."""
    holdings = []

    for line in holdings_text.splitlines():
        clean_line = line.split("//")[0].strip()

        if not clean_line:
            continue

        if clean_line.lower().replace(" ", "") == "ticker,shares,averagepurchaseprice":
            continue

        ticker, shares, average_cost = clean_line.split(",")

        holdings.append(
            {
                "Ticker": ticker.strip().upper(),
                "Shares": float(shares.strip()),
                "Average Cost": float(average_cost.strip()),
            }
        )

    return holdings


@st.cache_data(ttl=60)
def get_market_data(ticker):
    """Get current market data for one ticker."""
    stock = yf.Ticker(ticker)
    history = stock.history(period="5d")

    if history.empty:
        return None

    current_price = float(history["Close"].iloc[-1])
    previous_close = (
        float(history["Close"].iloc[-2])
        if len(history) > 1
        else current_price
    )

    daily_change = current_price - previous_close
    daily_change_percent = (daily_change / previous_close) * 100

    return {
        "Current Price": current_price,
        "Previous Close": previous_close,
        "Daily Change": daily_change,
        "Daily Change %": daily_change_percent,
    }


def color_gain(value):
    """Color positive numbers green and negative numbers red."""
    if value > 0:
        return "color: green"
    if value < 0:
        return "color: red"
    return ""


def apply_color_style(styler, columns):
    """Support both new and older pandas Styler versions."""
    if hasattr(styler, "map"):
        return styler.map(color_gain, subset=columns)
    return styler.applymap(color_gain, subset=columns)


st.sidebar.header("Your Holdings")
holdings_text = st.sidebar.text_area(
    "Enter one holding per line: TICKER, shares, average cost",
    value=DEFAULT_HOLDINGS,
    height=150,
)

auto_refresh = st.sidebar.checkbox("Auto-refresh page every 60 seconds", value=False)

if auto_refresh:
    st.markdown(
        "<meta http-equiv='refresh' content='60'>",
        unsafe_allow_html=True,
    )

if st.sidebar.button("Refresh prices now"):
    st.cache_data.clear()
    st.rerun()


try:
    holdings = parse_holdings(holdings_text)
except ValueError:
    st.error("Please enter holdings like this: AAPL,10,150")
    st.stop()


portfolio_rows = []

for holding in holdings:
    market_data = get_market_data(holding["Ticker"])

    if market_data is None:
        st.warning(f"Could not load market data for {holding['Ticker']}.")
        continue

    shares = holding["Shares"]
    average_cost = holding["Average Cost"]
    current_price = market_data["Current Price"]

    cost_basis = shares * average_cost
    market_value = shares * current_price
    gain_loss = market_value - cost_basis
    return_percent = (gain_loss / cost_basis) * 100

    portfolio_rows.append(
        {
            "Ticker": holding["Ticker"],
            "Shares": shares,
            "Average Cost": average_cost,
            "Current Price": current_price,
            "Previous Close": market_data["Previous Close"],
            "Daily Change": market_data["Daily Change"],
            "Daily Change %": market_data["Daily Change %"],
            "Cost Basis": cost_basis,
            "Market Value": market_value,
            "Gain/Loss": gain_loss,
            "Return %": return_percent,
        }
    )


if not portfolio_rows:
    st.info("Enter at least one valid holding to analyze your portfolio.")
    st.stop()


portfolio_df = pd.DataFrame(portfolio_rows)

total_cost_basis = portfolio_df["Cost Basis"].sum()
total_market_value = portfolio_df["Market Value"].sum()
total_gain_loss = total_market_value - total_cost_basis
total_return_percent = (total_gain_loss / total_cost_basis) * 100

portfolio_df["Allocation %"] = (
    portfolio_df["Market Value"] / total_market_value
) * 100

best_holding = portfolio_df.loc[portfolio_df["Return %"].idxmax()]
worst_holding = portfolio_df.loc[portfolio_df["Return %"].idxmin()]


st.subheader("Portfolio Summary")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cost Basis", f"${total_cost_basis:,.2f}")
col2.metric("Current Value", f"${total_market_value:,.2f}")
col3.metric("Total Gain/Loss", f"${total_gain_loss:,.2f}")
col4.metric("Total Return", f"{total_return_percent:.2f}%")

st.subheader("Performance Summary")

col1, col2 = st.columns(2)
col1.success(f"Best performer: {best_holding['Ticker']} ({best_holding['Return %']:.2f}%)")
col2.error(f"Worst performer: {worst_holding['Ticker']} ({worst_holding['Return %']:.2f}%)")

st.subheader("Holdings Detail")

styled_df = portfolio_df.style.format(
    {
        "Shares": "{:,.2f}",
        "Average Cost": "${:,.2f}",
        "Current Price": "${:,.2f}",
        "Previous Close": "${:,.2f}",
        "Daily Change": "${:,.2f}",
        "Daily Change %": "{:.2f}%",
        "Cost Basis": "${:,.2f}",
        "Market Value": "${:,.2f}",
        "Gain/Loss": "${:,.2f}",
        "Return %": "{:.2f}%",
        "Allocation %": "{:.2f}%",
    }
)

styled_df = apply_color_style(
    styled_df,
    ["Daily Change", "Daily Change %", "Gain/Loss", "Return %"],
)

st.dataframe(styled_df, use_container_width=True)

st.caption(
    "Daily change compares the latest available close to the previous close. "
    "During market hours, data timing depends on the provider and may be delayed."
)
