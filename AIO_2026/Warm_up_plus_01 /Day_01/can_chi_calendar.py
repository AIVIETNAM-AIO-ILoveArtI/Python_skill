def calculate_can_chi_calendar ( year ) :
    result = ''
    #tạo biến lưu kết quả
    can = ['Canh','Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
    #tạo list can
    chi = ['Thân','Dậu','Tuất','Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn' ,'Tỵ', 'Ngọ', 'Mùi']
    #tạo list chi
    result = can[year%10]+' '+chi[year%12]
    #year%10 tương đương chỉ ra index của can tương đương theo year mà lắp vào biến
    #year%12 tương đương chỉ ra index của chi tương đương theo year mà lắp vào biến
    #can[year%10],chi[year%12] truy cập vào phần tử dựa trên index đã chỉ ra
    return result
    #trả về kết quả(nếu không trả về thì sẽ không hiện kết quả đã lưu)

print(calculate_can_chi_calendar(2024))
print(calculate_can_chi_calendar(2023))
print(calculate_can_chi_calendar(1997))
#in kết quả theo đề bài
