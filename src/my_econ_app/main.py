import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data() -> pd.DataFrame:
    """株価・為替データを取得する"""
    tickers = {
        'USDJPY=X': 'USD/JPY',
        '^N225': 'Nikkei 225',
        '^GSPC': 'S&P 500'
    }
    df = yf.download(list(tickers.keys()), period="1y")['Close']
    df = df.rename(columns=tickers)
    df = df.ffill().bfill()
    return df

def calculate_stats(df: pd.DataFrame) -> pd.DataFrame:
    """基本統計量を計算する"""
    return pd.DataFrame({
        'Mean': df.mean(),
        'Min': df.min(),
        'Max': df.max(),
    })

def save_report_plot(df: pd.DataFrame, filename: str = "econ_report.pdf") -> None:
    """正規化したデータをベクター形式（PDF）で保存する"""
    normalized = (df / df.iloc[0]) * 100
    
    fig, ax = plt.subplots(figsize=(8, 4))
    for col in normalized.columns:
        ax.plot(normalized.index, normalized[col], label=col)
    
    ax.set_title("Economic Indicators Index (Base = 100)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Index Value")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="best")
    
    plt.tight_layout()
    fig.savefig(filename, format="pdf")
    plt.close()

def main():
    print("Fetching economic data...")
    df = fetch_data()
    
    print("Calculating statistics...")
    stats = calculate_stats(df)
    print("\n--- Summary Statistics ---")
    print(stats)
    
    print("\nGenerating PDF report...")
    save_report_plot(df, "econ_report.pdf")
    print("Done! Report saved as 'econ_report.pdf'.")

if __name__ == "__main__":
    main()