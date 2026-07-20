import pandas as pd
import numpy as np
from my_econ_app.main import calculate_stats

def test_calculate_stats():
    # テスト用のダミーデータを作成
    dates = pd.date_range("2026-01-01", periods=3)
    dummy_df = pd.DataFrame({
        'USD/JPY': [150.0, 152.0, 151.0],
        'S&P 500': [5000.0, 5100.0, 5050.0]
    }, index=dates)
    
    # 計算処理を実行
    stats = calculate_stats(dummy_df)
    
    # 期待通りの数値（平均・最小・最大）になっているか検証
    assert np.isclose(stats.loc['USD/JPY', 'Mean'], 151.0)
    assert stats.loc['USD/JPY', 'Min'] == 150.0
    assert stats.loc['USD/JPY', 'Max'] == 152.0