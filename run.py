from osgeo import gdal, osr

def set_geotransform(input_tiff, output_tiff, top_left_lon, top_left_lat, bottom_right_lon, bottom_right_lat):
    # Mở file TIFF gốc
    src_ds = gdal.Open(input_tiff, gdal.GA_ReadOnly)
    if src_ds is None:
        print("Không thể mở file ảnh:", input_tiff)
        return

    # Lấy kích thước của ảnh
    width = src_ds.RasterXSize
    height = src_ds.RasterYSize

    # Tính toán giá trị GeoTransform
    pixel_width = (bottom_right_lon - top_left_lon) / width
    pixel_height = -(top_left_lat - bottom_right_lat) / height  # Đảm bảo giá trị là âm

    geo_transform = (top_left_lon, pixel_width, 0, top_left_lat, 0, pixel_height)

    # Thiết lập hệ tọa độ (WGS84)
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)

    # Tạo file đầu ra và áp dụng GeoTransform và hệ tọa độ
    driver = gdal.GetDriverByName('GTiff')
    dst_ds = driver.Create(output_tiff, width, height, src_ds.RasterCount, src_ds.GetRasterBand(1).DataType)
    dst_ds.SetGeoTransform(geo_transform)
    dst_ds.SetProjection(srs.ExportToWkt())

    # Sao chép dữ liệu từ ảnh gốc sang ảnh mới
    for i in range(src_ds.RasterCount):
        src_band = src_ds.GetRasterBand(i + 1)
        dst_band = dst_ds.GetRasterBand(i + 1)
        dst_band.WriteArray(src_band.ReadAsArray())

    # Lưu và đóng file
    dst_ds = None
    src_ds = None
    print(f"Geo-referencing hoàn tất. File được lưu tại: {output_tiff}")

# Đường dẫn file gốc và file đầu ra
input_tiff = r'C:\Users\nghiant\Downloads\Vi\Ok.tif'
output_tiff = r'C:\Users\nghiant\Downloads\Vi\out.tif'

# Tọa độ
top_left_lon = 106.38830514778901
top_left_lat = 10.306124377544664
bottom_right_lon = 106.41686307128403
bottom_right_lat = 10.290724465762292

# Chạy hàm
set_geotransform(input_tiff, output_tiff, top_left_lon, top_left_lat, bottom_right_lon, bottom_right_lat)
