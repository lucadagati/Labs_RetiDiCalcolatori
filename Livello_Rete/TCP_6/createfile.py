file_size = 10 * 1024 * 1024  # 10 MB
with open('your_file_to_send', 'wb') as f:
    f.write(b'0' * file_size)
