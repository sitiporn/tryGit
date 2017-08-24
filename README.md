# Test github
Test1 Test2 Test3 Test4 Test5 Test6

### สรุปคำสั่ง ตอนนี้ `24/08/2560`
ใช้ git ในไฟล์โปรเจกเรา
> git init

ดู status
> git status

เเล้ว remote ไปที่ github repository ของเราที่สร้างเเล้ว
> git remote add origin url...

ทำการ add file_code , tabเอา
> git add file_name file_name2 ...

เมื่อมีการเเก้ไข code ที่ลองมาเเล้วต้อง add เเล้ว commit ก่อน
> git commit -m "บอกไปว่ากำลังทำอะไร หรือเเก้อะไร"

จากนั้นก็ push ขึ้น server github ของเราได้ละ
> git push -u origin master

ตามด้วย username and password
จบส่วนการ update code ขึ้น github

ส่วนการ pull หรือ load code ลงมาที่ local
ตรวจดูการเปลี่ยนเเปลงก่อน
> git fetch

จากนั้น merge มาหาโฟลเดอร์เรา
> git merge origin/master

พอได้ไฟล์อัพเดทมาเเล้ว ลองดู status รู้สึกว่าต้อง add ก่อน
เเต่ถ้ามีปัญหา Conflict ก็ต้องเเก้ก่อน อันนี้ยังงงๆ ว่ามัน conflict ตอนอัพไฟล์ขึ้นไปด้วยใช่ไหม?

### คำสั่งอื่นๆ
ดูประวัติ
> git log

ดูเเละสร้าง branch
> git branch 

หรือ สร้างเเละสลับในคำสังเดียว
> git checkout -b branch_new_name

ลบ branch
> git branch -d branch_name

สลับ branch
> git checkout branch_name

ทำ merge ระหว่าง branch ได้ด้วย
> git merge branch_name



