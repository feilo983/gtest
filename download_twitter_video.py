import yt_dlp
import os

def download_twitter_video(tweet_url):
    # 创建下载目录
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # 设置下载选项
    ydl_opts = {
        'format': 'best',  # 下载最好的质量
        'outtmpl': 'downloads/%(id)s.%(ext)s',  # 输出模板
        'progress_hooks': [lambda d: print(f"\r下载进度: {d['_percent_str']}", end='') if d['status'] == 'downloading' else None],
    }
    
    try:
        # 创建下载器
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 下载视频
            print("开始下载视频...")
            ydl.download([tweet_url])
            print("\n下载完成！")
    except Exception as e:
        print(f"下载出错: {str(e)}")

if __name__ == "__main__":
    tweet_url = "https://x.com/techartist_/status/1912132028406866378"
    download_twitter_video(tweet_url)