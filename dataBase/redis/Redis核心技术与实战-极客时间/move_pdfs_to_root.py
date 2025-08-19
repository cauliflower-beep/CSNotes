import os
import shutil

def move_pdfs_to_root():
    # 获取当前工作目录（根目录）
    root_dir = os.getcwd()
    
    # 遍历所有子文件夹
    for dirpath, _, filenames in os.walk(root_dir):
        # 跳过根目录本身
        if dirpath == root_dir:
            continue
            
        # 检查每个文件
        for filename in filenames:
            # 如果是 PDF 文件
            if filename.lower().endswith('.pdf'):
                # 构建源文件路径
                source_path = os.path.join(dirpath, filename)
                # 构建目标文件路径（根目录）
                dest_path = os.path.join(root_dir, filename)
                
                # 检查目标路径是否已存在同名文件
                if os.path.exists(dest_path):
                    # 如果存在，添加数字后缀以避免覆盖
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_filename = f"{base}_{counter}{ext}"
                        dest_path = os.path.join(root_dir, new_filename)
                        counter += 1
                
                try:
                    # 移动文件
                    shutil.move(source_path, dest_path)
                    print(f"已移动: {filename} -> {root_dir}")
                except Exception as e:
                    print(f"移动 {filename} 时出错: {str(e)}")

if __name__ == "__main__":
    move_pdfs_to_root()