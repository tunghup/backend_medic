-- 1. Thêm UserProfile 
INSERT INTO UserProfile (user_id, phone_number, id_number, university, major, graduation_year, birth_date, role, is_manager)
VALUES
(1, '0901234567', '123456789', 'ĐH Y Dược TP.HCM', 'Y đa khoa', 2015, '1990-01-01', 'Bác sĩ', TRUE),
(2, '0912345678', '234567890', 'ĐH Y Dược Cần Thơ', 'Dược', 2016, '1991-02-15', 'Dược sĩ', FALSE),
(3, '0923456789', '345678901', 'ĐH Y Hà Nội', 'Điều dưỡng', 2017, '1992-03-20', 'Lễ tân', FALSE),
(4, '0934567890', '456789012', 'ĐH Y Dược Huế', 'Răng hàm mặt', 2014, '1989-04-10', 'Bác sĩ', FALSE),
(5, '0945678901', '567890123', 'ĐH Y Dược TP.HCM', 'Y học cổ truyền', 2013, '1988-05-25', 'Quản lý', TRUE);

-- 2. MedicalSupply
INSERT INTO MedicalSupply (code, name, quantity, unit, expiration_date, description, supplier, threshold, unit_price)
VALUES
('MS001', 'Khẩu trang y tế', 500, 'Hộp', '2026-01-01', 'Khẩu trang dùng 1 lần', 'Công ty Dược ABC', 100, 50000),
('MS002', 'Găng tay cao su', 300, 'Hộp', '2025-12-31', 'Găng tay y tế không bột', 'Công ty Dược XYZ', 50, 75000);

-- 3. Patient
INSERT INTO Patient (full_name, gender, birth_date, address, phone_number, id_card, has_insurance, insurance_code,
symptoms, allergy, medical_history, current_medications, old_test_results)
VALUES
('Nguyễn Văn A', 'Nam', '1985-01-01', '123 Lê Lợi, Q1', '0909999999', '012345678', TRUE, 'BH001', 'Ho, sốt', 'Không', 'Hen suyễn', '', ''),
('Trần Thị B', 'Nữ', '1990-02-02', '456 Trần Hưng Đạo, Q5', '0918888888', '023456789', FALSE, NULL, 'Đau bụng', 'Penicillin', 'Viêm dạ dày', 'Paracetamol', '');

-- 4. TreatmentRecord
INSERT INTO TreatmentRecord (patient_id, symptoms, blood_pressure_systolic, blood_pressure_diastolic, pulse, spo2, temperature, current_medications, old_test_results)
VALUES
(1, 'Ho, sốt nhẹ', 120, 80, 78, 98, 37.2, '', ''),
(2, 'Đau bụng âm ỉ', 110, 70, 75, 99, 36.8, 'Paracetamol', '');

-- 5. TestResult
INSERT INTO TestResult (patient_id, test_type, result_value, unit, ecg_result, ultrasound_result, price)
VALUES
(1, 'Đường huyết mao mạch', 5.8, 'mmol/L', NULL, NULL, 80000),
(2, 'Siêu âm', NULL, NULL, NULL, 'Không phát hiện bất thường', 150000);

-- 6. InventoryTransaction
INSERT INTO InventoryTransaction (supply_id, transaction_type, quantity, note)
VALUES
(1, 'Xuất kho', 50, 'Cấp phát cho phòng khám'),
(2, 'Nhập kho', 100, 'Nhập từ nhà cung cấp');

-- 7. Invoice
INSERT INTO Invoice (patient_id, total_amount, details)
VALUES
(1, 230000, 'Khám + xét nghiệm'),
(2, 150000, 'Siêu âm');

-- 8. TaiKhoan (tài khoản đăng nhập)
INSERT INTO TaiKhoan (TenDangNhap, MatKhau, VaiTro)
VALUES
('admin', 'admin123', 'Quản lý'),
('bacsi01', 'abc@123A', 'Bác sĩ'),
('letan01', 'abc@123A', 'Lễ tân'),
('duocsi01', 'abc@123A', 'Dược sĩ'),
('thuongtru01', 'abc@123A', 'Thường trực');
