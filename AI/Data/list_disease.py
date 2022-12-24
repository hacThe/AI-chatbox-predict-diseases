disease = [
    {
        'drug reaction': {
            'vie': 'phản ứng thuốc', 
            'precaution': ['ngừng kích thích', 'đến bệnh viện gần nhất', 'ngừng dùng thuốc', 'theo dõi tình trạng bản thân']
        }
    },
    {
        'malaria': {
            'vie': 'bệnh sốt rét', 
            'precaution': ['đến bệnh viện gần nhất', 'tránh thức ăn nhờn', 'tránh thức ăn không rau', 'giữ muỗi ra']
        }
    },
    {
        'allergy': {
            'vie': 'dị ứng',
            'precaution': ['áp dụng calamine', 'khu vực che phủ băng', 'sử dụng băng để nén ngứa']
        }
    },
    {'hypothyroidism': {'vie': 'suy giáp', 'precaution': [
        'giảm căng thẳng', 'bài tập', 'ăn uống lành mạnh', 'ngủ đúng cách']}},
    {'psoriasis': {'vie': 'bệnh vẩy nến', 'precaution': [
        'rửa tay bằng nước xà phòng ấm', 'ngừng chảy máu bằng áp lực', 'lắng nghe ý kiến bác sĩ', 'tắm muối']}},
    {'gerd': {'vie': 'gerd', 'precaution': [
        'tránh thức ăn cay béo', 'tránh nằm xuống sau khi ăn', 'duy trì cân nặng khỏe mạnh', 'bài tập']}},
    {'chronic cholestasis': {'vie': 'cholestocation mãn tính', 'precaution': [
        'tắm lạnh', 'thuốc chống ngứa', 'lắng nghe ý kiến bác sĩ', 'ăn uống lành mạnh']}},
    {'hepatitis a': {'vie': 'viêm gan a.', 'precaution': [
        'đến bệnh viện gần nhất', 'rửa tay qua', 'tránh thức ăn cay béo', 'thuốc']}},
    {'osteoarthristis': {'vie': 'xương khớp', 'precaution': [
        'acetaminophen', 'đến bệnh viện gần nhất', 'theo dõi tình trạng bản thân', 'tắm muối']}},
    {'(vertigo) paroymsal  positional vertigo': {'vie': '(vertigo) vertigo vị trí paroymsal', 'precaution': [
        'nằm xuống', 'tránh thay đổi đột ngột trong cơ thể', 'tránh di chuyển đầu đột ngột', 'thư giãn']}},
    {'hypoglycemia': {'vie': 'hạ đường huyết', 'precaution': [
        'nằm xuống bên', 'kiểm tra xung', 'uống đồ uống có đường', 'lắng nghe ý kiến bác sĩ']}},
    {'acne': {'vie': 'mụn', 'precaution': [
        'tắm hai lần', 'tránh thức ăn cay béo', 'uống nhiều nước', 'tránh quá nhiều sản phẩm']}},
    {'diabetes': {'vie': 'bệnh tiểu đường', 'precaution': [
        'có chế độ ăn uống cân bằng', 'bài tập', 'lắng nghe ý kiến bác sĩ', 'theo dõi tình trạng bản thân']}},
    {'impetigo': {'vie': 'vụ đông', 'precaution': ['ngâm khu vực bị ảnh hưởng trong nước ấm',
                                                   'sử dụng kháng sinh', 'loại bỏ các vảy bằng vải nén ướt', 'lắng nghe ý kiến bác sĩ']}},
    {'hypertension': {'vie': 'tăng huyết áp', 'precaution': [
        'thiền', 'tắm muối', 'giảm căng thẳng', 'ngủ đúng cách']}},
    {'peptic ulcer diseae': {'vie': 'loét peptic', 'precaution': [
        'tránh thức ăn cay béo', 'tiêu thụ thực phẩm sinh học', 'loại bỏ sữa', 'giới hạn rượu']}},
    {'dimorphic hemmorhoids(piles)': {'vie': 'hemmorhoid lưỡng hình (cọc)', 'precaution': [
        'tránh thức ăn cay béo', 'tiêu thụ phù thủy hazel', 'tắm ấm với muối epsom', 'tiêu thụ nước ép alovera']}},
    {'common cold': {'vie': 'cảm lạnh thông thường', 'precaution': [
        'uống vitamin c đồ uống giàu', 'lấy hơi', 'tránh thức ăn lạnh', 'giữ sốt khi kiểm tra']}},
    {'chicken pox': {'vie': 'thủy đậu', 'precaution': [
        'sử dụng neem trong tắm', 'tiêu thụ lá neem', 'lấy vắc -xin', 'tránh những nơi công cộng']}},
    {'cervical spondylosis': {'vie': 'viêm thắt cổ tử cung', 'precaution': [
        'sử dụng miếng đệm sưởi hoặc gói lạnh', 'bài tập', 'uống otc pain reliver', 'lắng nghe ý kiến bác sĩ']}},
    {'hyperthyroidism': {'vie': 'cường giáp', 'precaution': [
        'ăn uống lành mạnh', 'mát xa', 'sử dụng balm chanh', 'điều trị bằng iốt phóng xạ']}},
    {'urinary tract infection': {'vie': 'nhiễm trùng đường tiết niệu', 'precaution': [
        'uống nhiều nước', 'tăng lượng vitamin c', 'uống nước ép nam việt quất', 'uống men vi sinh']}},
    {'varicose veins': {'vie': 'suy tĩnh mạch', 'precaution': [
        'nằm xuống bằng phẳng và nâng chân cao', 'sử dụng oinment', 'sử dụng nén tĩnh mạch', 'đừng đứng yên lâu rồi']}},
    {'aids': {'vie': 'aids', 'precaution': [
        'tránh cắt mở', 'mặc ppe nếu có thể', 'lắng nghe ý kiến bác sĩ', 'theo dõi tình trạng bản thân']}},
    {'paralysis (brain hemorrhage)': {'vie': 'tê liệt (xuất huyết não)', 'precaution': [
        'mát xa', 'ăn uống lành mạnh', 'bài tập', 'lắng nghe ý kiến bác sĩ']}},
    {'typhoid': {'vie': 'bệnh thương hàn', 'precaution': [
        'ăn nhiều calo vegitables', 'liệu pháp kháng sinh', 'lắng nghe ý kiến bác sĩ', 'thuốc']}},
    {'hepatitis b': {'vie': 'bệnh viêm gan b', 'precaution': [
        'đến bệnh viện gần nhất', 'tiêm chủng', 'ăn uống lành mạnh', 'thuốc']}},
    {'fungal infection': {'vie': 'nhiễm trùng nấm', 'precaution': [
        'tắm hai lần', 'sử dụng detol hoặc neem trong nước tắm', 'giữ cho khu vực bị nhiễm khô', 'sử dụng vải sạch']}},
    {'hepatitis c': {'vie': 'viêm gan c.', 'precaution': [
        'đến bệnh viện gần nhất', 'tiêm chủng', 'ăn uống lành mạnh', 'thuốc']}},
    {'migraine': {'vie': 'đau nửa đầu', 'precaution': [
        'thiền', 'giảm căng thẳng', 'sử dụng kính poloroid trong ánh nắng mặt trời', 'lắng nghe ý kiến bác sĩ']}},
    {'bronchial asthma': {'vie': 'hen phế quản', 'precaution': [
        'chuyển sang cảm ứng lỏng lẻo', 'lấy hơi thở sâu', 'tránh xa kích hoạt', 'tìm kiếm sự giúp đỡ']}},
    {'alcoholic hepatitis': {'vie': 'viêm gan do rượu', 'precaution': [
        'ngừng tiêu thụ rượu', 'lắng nghe ý kiến bác sĩ', 'thuốc', 'theo dõi tình trạng bản thân']}},
    {'jaundice': {'vie': 'vàng da', 'precaution': [
        'uống nhiều nước', 'tiêu thụ cây kế sữa', 'ăn trái cây và thức ăn nhiều chất xơ', 'thuốc']}},
    {'hepatitis e': {'vie': 'viêm gan e', 'precaution': [
        'ngừng tiêu thụ rượu', 'nghỉ ngơi', 'lắng nghe ý kiến bác sĩ', 'thuốc']}},
    {'dengue': {'vie': 'sốt xuất huyết', 'precaution': [
        'uống nước đu đủ', 'tránh thức ăn cay béo', 'giữ muỗi đi', 'giữ nước']}},
    {'hepatitis d': {'vie': 'viêm gan d', 'precaution': [
        'lắng nghe ý kiến bác sĩ', 'thuốc', 'ăn uống lành mạnh', 'theo dõi tình trạng bản thân']}},
    {'heart attack': {'vie': 'đau tim', 'precaution': [
        'gọi xe cứu thương', 'nhai hoặc nuốt asprin', 'giữ bình tĩnh']}},
    {'pneumonia': {'vie': 'viêm phổi', 'precaution': [
        'lắng nghe ý kiến bác sĩ', 'thuốc', 'nghỉ ngơi', 'theo dõi tình trạng bản thân']}},
    {'arthritis': {'vie': 'viêm khớp', 'precaution': [
        'bài tập', 'sử dụng liệu pháp nóng và lạnh', 'hãy thử châm cứu', 'mát xa']}},
    {'gastroenteritis': {'vie': 'viêm tiêu hóa', 'precaution': [
        'ngừng ăn thức ăn đặc trong khi', 'hãy thử uống những ngụm nước nhỏ', 'nghỉ ngơi', 'dễ dàng trở lại ăn uống']}},
    {'tuberculosis': {'vie': 'bệnh lao', 'precaution': [
        'che miệng', 'lắng nghe ý kiến bác sĩ', 'thuốc', 'nghỉ ngơi']}}
]
