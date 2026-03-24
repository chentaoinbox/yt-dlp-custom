import os
import zipfile
import tarfile
import platform
import urllib.request
import shutil


def setffmpeg():
    system = platform.system().lower()
    arch = platform.machine().lower()
    
    if system == "windows":
        zip_path = "ffmpeg.zip"
        urllib.request.urlretrieve(
            "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",
            zip_path
        )
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall()
        
        for d in os.listdir():
            if os.path.isdir(d) and d.startswith("ffmpeg"):
                shutil.move(d, "ffmpeg")
        
        os.remove(zip_path)
        return "ffmpeg/bin/"
    
    elif system == "linux":
        if arch in ["x86_64", "amd64"]:
            url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
        elif arch in ["aarch64", "arm64"]:
            url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-arm64-static.tar.xz"
        else:
            url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-armhf-static.tar.xz"
        
        tar_path = "ffmpeg.tar.xz"
        urllib.request.urlretrieve(url, tar_path)
        
        with tarfile.open(tar_path, 'r:xz') as tf:
            tf.extractall()
        
        for d in os.listdir():
            if os.path.isdir(d) and d.startswith("ffmpeg"):
                shutil.move(d, "ffmpeg")
        
        os.remove(tar_path)
        os.chmod("ffmpeg/ffmpeg", 0o755)
        return "ffmpeg/ffmpeg"
    
    elif system == "darwin":  # macOS
        arch = "arm64" if arch == "arm64" else "intel"
        url = f"https://www.osxexperts.net/ffmpeg{arch}.zip"
        
        zip_path = "ffmpeg.zip"
        urllib.request.urlretrieve(url, zip_path)
        
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall()
        
        for d in os.listdir():
            if os.path.isdir(d) and d.startswith("ffmpeg"):
                shutil.move(d, "ffmpeg")
        
        os.remove(zip_path)
        os.chmod("ffmpeg/ffmpeg", 0o755)
        return "ffmpeg/ffmpeg"
    
    return None


def setnodejs():
    system = platform.system().lower()
    arch = platform.machine().lower()
    version = "22.14.0"
    
    if system == "windows":
        zip_path = "node.zip"
        urllib.request.urlretrieve(
            f"https://nodejs.org/dist/v{version}/node-v{version}-win-x64.zip",
            zip_path
        )
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall()
        
        for d in os.listdir():
            if os.path.isdir(d) and d.startswith("node-v"):
                shutil.move(d, "node")
        
        os.remove(zip_path)
        return "node/node_modules/npm/bin"
    
    elif system == "linux":
        if arch in ["x86_64", "amd64"]:
            filename = f"node-v{version}-linux-x64.tar.xz"
        elif arch in ["aarch64", "arm64"]:
            filename = f"node-v{version}-linux-arm64.tar.xz"
        else:
            filename = f"node-v{version}-linux-armv7l.tar.xz"
        
        url = f"https://nodejs.org/dist/v{version}/{filename}"
        tar_path = filename
        urllib.request.urlretrieve(url, tar_path)
        
        with tarfile.open(tar_path, 'r:xz') as tf:
            tf.extractall()
        
        for d in os.listdir():
            if os.path.isdir(d) and d.startswith("node-v"):
                shutil.move(d, "node")
        
        os.remove(tar_path)
        os.chmod("node/node_modules/npm/bin", 0o755)
        return "node/node_modules/npm/bin"
    
    elif system == "darwin":  # macOS
        arch = "arm64" if arch == "arm64" else "x64"
        filename = f"node-v{version}-darwin-{arch}.tar.gz"
        url = f"https://nodejs.org/dist/v{version}/{filename}"
        tar_path = filename
        urllib.request.urlretrieve(url, tar_path)
        
        with tarfile.open(tar_path, 'r:gz') as tf:
            tf.extractall()
        
        for d in os.listdir():
            if os.path.isdir(d) and d.startswith("node-v"):
                shutil.move(d, "node")
        
        os.remove(tar_path)
        os.chmod("node/node_modules/npm/bin", 0o755)
        return "node/node_modules/npm/bin"
    
    return None


# 使用
if __name__ == "__main__":
    ffmpeg = setffmpeg()
    node = setnodejs()
    print(f"FFmpeg: {ffmpeg}")
    print(f"Node.js: {node}")