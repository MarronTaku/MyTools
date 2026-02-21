import torch
import time

# MPS (Metal Performance Shaders) が利用可能か確認
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print(f"✅ Apple Silicon GPU (MPS) is available!")
    print(f"Device: {device}")
    
    # 簡単な計算テスト
    try:
        # GPU上にランダムなテンソルを作成
        x = torch.randn(1000, 1000, device=device)
        y = torch.randn(1000, 1000, device=device)
        
        start = time.time()
        # 行列積を計算
        z = torch.matmul(x, y)
        # 同期をとる（GPU処理の完了を待つ）
        torch.mps.synchronize() 
        end = time.time()
        
        print(f"Calculation finished in {end - start:.4f} seconds.")
        print("Setup is complete.")
    except Exception as e:
        print(f"Error during calculation: {e}")

else:
    print("❌ MPS is not available. Check your PyTorch installation.")
