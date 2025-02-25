# Danh sách thư mục chứa email rác (spam)
spam_folders = [
    "C:\\Users\\Admin\\Downloads\\spam_2\\spam_2",

]

# Danh sách thư mục chứa email thường (ham)
ham_folders = [
    "C:\\Users\\Admin\\Downloads\\easy_ham\\easy_ham",

]
import os
import glob

mail_data = []  # list để lưu (nội_dung, nhãn)

# Đọc thư mục SPAM
for folder_path in spam_folders:
    spam_files = glob.glob(os.path.join(folder_path, "*"))

    for fname in spam_files:
        try:
            with open(fname, "r", encoding="latin-1") as f:
                content = f.read()
            mail_data.append((content, 1))
        except:
            pass  # nếu file bị lỗi đọc thì bỏ qua

# Đọc thư mục HAM
for folder_path in ham_folders:
    ham_files = glob.glob(os.path.join(folder_path, "*"))

    for fname in ham_files:
        try:
            with open(fname, "r", encoding="latin-1") as f:
                content = f.read()
            # Thêm vào list mail_data, label=0 (ham)
            mail_data.append((content, 0))
        except:
            pass

import pandas as pd

df = pd.DataFrame(mail_data, columns=["text", "label"])
print(df.head())
print(df['label'].value_counts())


df.to_csv("spamassassin_data.csv", index=False)
print(df['label'].value_counts())
df.drop_duplicates(subset='text', keep='first', inplace=True)
df = df[df['text'].str.len() > 10]  # bỏ email dưới 10 ký tự, ví dụ
import pandas as pd

# Giả sử DataFrame của bạn là df
print("Số lượng email ban đầu:", df.shape[0])

# Loại bỏ trùng lặp dựa trên nội dung email
df.drop_duplicates(subset='text', inplace=True)

print("Số lượng email sau khi loại bỏ trùng lặp:", df.shape[0])
# Loại bỏ email có độ dài dưới 20 ký tự (tùy chỉnh)
df = df[df['text'].str.len() > 20]

print("Số lượng email sau khi loại bỏ email quá ngắn:", df.shape[0])
# Kiểm tra giá trị thiếu
print(df.isnull().sum())

# Loại bỏ các dòng có giá trị thiếu
df.dropna(subset=['text', 'label'], inplace=True)

print("Số lượng email sau khi loại bỏ giá trị thiếu:", df.shape[0])
print(df['label'].value_counts())
print("Hãy nhập số luongj email của bạn")


# Chia dữ liệu thành X và y
X = df['text']
y = df['label']

