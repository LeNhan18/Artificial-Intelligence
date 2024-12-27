Artificial Neural Network
Linear Function (Hàm tuyến tính):
Là một hàm đại số cụ thể được thể hiện mối quan  hệ tuyến tính  giữa hai biến 
f(x)=mx+c






Non-Linear Function (Hàm phi tuyến tính):
Là hàm mà mối quan hệ giữa các biến mà không phải đường thẳng. Nói cách khác tốc độ thay đổi của hàm không nhất quán tại mọi điểm

f(x)=ax2+bx+c
f(x) = \sin(x), \quad f(x) = e^x, \quad f(x) = \log(x) \quad 
f(x)=sin(x),f(x)=ex,f(x)=log(x)





Artificial Neural Networks

Artificial Neural Networks contain artificial neurons which are called units . These units are arranged in a series of layers that together constitute the whole Artificial Neural Network in a system. A layer can have only a dozen units or millions of units as this depends on how the complex neural networks will be required to learn the hidden patterns in the data set. Commonly, Artificial Neural Network has an input layer, an output layer as well as hidden layers. The input layer receives data from the outside world which the neural network needs to analyze or learn about. Then this data passes through one or multiple hidden layers that transform the input into data that is valuable for the output layer. Finally, the output layer provides an output in the form of a response of the Artificial Neural Networks to input data provided.
In the majority of neural networks, units are interconnected from one layer to another. Each of these connections has weights that determine the influence of one unit on another unit. As the data transfers from one unit to another, the neural network learns more and more about the data which eventually results in an output from the output layer.
( Mạng nơ ron nhân tạo chứa các nơ ron nhân tạo gọi là các đơn vị. Các đơn vị này được sắp xếp thành một loạt các lớp cùng nhau tạo nên toàn bộ mạng nơ ron nhân tạo trên hệ thống Một lớp chỉ có thể có một tá đơn vị hoặc hàng triệu đơn vị vì điều này phụ thuộc vào cách các mạng nơ-ron phức tạp sẽ được yêu cầu để học các mẫu ẩn trong tập dữ liệu. Thông thường, Mạng nơ-ron nhân tạo có một lớp đầu vào, một lớp đầu ra cũng như các lớp ẩn. Lớp đầu vào nhận dữ liệu từ thế giới bên ngoài mà mạng nơ-ron cần phân tích hoặc tìm hiểu. Sau đó, dữ liệu này đi qua một hoặc nhiều lớp ẩn để chuyển đổi đầu vào thành dữ liệu có giá trị cho lớp đầu ra. Cuối cùng, lớp đầu ra cung cấp đầu ra dưới dạng phản hồi của Mạng nơ-ron nhân tạo đối với dữ liệu đầu vào được cung cấp
Trong phần lớn các mạng nơ-ron, các đơn vị được kết nối với nhau từ lớp này sang lớp khác. Mỗi kết nối này có trọng số xác định ảnh hưởng của một đơn vị lên một đơn vị khác. Khi dữ liệu được truyền từ đơn vị này sang đơn vị khác, mạng nơ-ron học ngày càng nhiều về dữ liệu, cuối cùng dẫn đến đầu ra từ lớp đầu ra. )



Thuật Toán lan truyền ngược
(Backpropagation)
Lan truyền ngược là một kỹ thuật học máy cần thiết để tối ưu hóa mạng lưới thần kinh nhân tạo. Nó tạo điều kiện thuận lợi cho việc sử dụng các thuật toán giảm độ dốc để cập nhật trọng số mạng, đó là cách các mô hình học sâu thúc đẩy trí tuệ nhân tạo (AI) hiện đại "học".

Thuật toán Backpropagation là 1 thuật toán dùng đạo hàm ngược (reverse of  differentiation) được áp dụng trong Artificial Neural Network giúp tính các đạo hàm cần thiết để tối ưu hóa các tham số trong mô hình 


∂b1(1)​∂L​=∂a1(1)​∂L​∗∂b1(1)​∂a1(1)​​
Một số biến thể cải tiến của thuật toán :
Weight Decay: Kỹ Thuật này giúp tránh overfiting
