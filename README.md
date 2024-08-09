# add-viewbox-tiff
Hình ảnh dạng tiff mà chưa có viewbox, chương trình sẽ hướng dẫn add vào

## Cài đặt
### Cài đặt GDAL
Download gdal tại https://gdal.org/download.html chọn hệ điều hành để tải hoặc có thể truy cập trực tiếp vào https://www.anaconda.com/download/success

### Sau khi download xong thì tiến hành cài đặt
Cài đặt chú ý setup biến môi trường luôn

### Mở chương trình
1. Click vào Window -> Anaconda Prompt Gõ lệnh `conda install -c conda-forge gdal`
2. Kiểm tra python `python --version` nếu hiển thị thông tin version python là Ok
3. Sửa file run.py có input_tiff(file đầu vào), top_left_lon, top_left_lat, bottom_right_lon, bottom_right_lat viewbox cho hợp lý, output_tiff(file tiff đầu ra)
4. Chạy chương trình gõ lệnh `python run.py`

### Support nếu bị lỗi
Nếu bị lỗi thi cần có thể liên hệ email thanhnghiacntt@gmail.com để hỗ trợ


